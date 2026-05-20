from flask import Flask, render_template, request, redirect, url_for
import os
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

app = Flask(__name__)
# The database file will be created in the current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stitch.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db, User, Task, Event, JobApplication, StudySession, ChatMessage

db.init_app(app)

with app.app_context():
    db.create_all()
    # Auto-seed the database if no User exists to prevent crash on spin-up
    if User.query.first() is None:
        try:
            from seed_db import seed_database
            seed_database(app_instance=app, drop_existing=False)
            print("Database was empty. Auto-seeded initial data successfully!")
        except Exception as e:
            app.logger.error(f"Error auto-seeding database: {e}")

@app.route('/')
def index():
    user = User.query.first()
    tasks = Task.query.filter_by(user_id=user.id).order_by(Task.priority).all()
    events = Event.query.filter_by(user_id=user.id).all()
    jobs = JobApplication.query.filter_by(user_id=user.id).all()
    return render_template('dashboard.html', user=user, tasks=tasks, events=events, jobs=jobs)

@app.route('/calendar')
def calendar():
    user = User.query.first()
    events = Event.query.filter_by(user_id=user.id).all()
    return render_template('calendar.html', user=user, events=events)

@app.route('/roadmap')
def roadmap():
    user = User.query.first()
    tasks = Task.query.filter_by(user_id=user.id).order_by(Task.priority).all()
    return render_template('roadmap.html', user=user, tasks=tasks)

@app.route('/applications')
def applications():
    user = User.query.first()
    jobs = JobApplication.query.filter_by(user_id=user.id).order_by(JobApplication.applied_date.desc()).all()
    return render_template('applications.html', user=user, jobs=jobs)

@app.route('/progress')
def progress():
    user = User.query.first()
    tasks = Task.query.filter_by(user_id=user.id).all()
    jobs = JobApplication.query.filter_by(user_id=user.id).all()
    sessions = StudySession.query.filter_by(user_id=user.id).all()
    return render_template('progress.html', user=user, tasks=tasks, jobs=jobs, sessions=sessions)

@app.route('/timer')
def timer():
    user = User.query.first()
    return render_template('timer.html', user=user)

@app.route('/chatbot')
def chatbot():
    user = User.query.first()
    messages = ChatMessage.query.filter_by(user_id=user.id).order_by(ChatMessage.timestamp).all()
    return render_template('chatbot.html', user=user, messages=messages)

# --- CRUD Handlers ---

@app.route('/add_task', methods=['POST'])
def add_task():
    user = User.query.first()
    title = request.form.get('title')
    priority = request.form.get('priority', 1, type=int)
    if title:
        new_task = Task(user_id=user.id, title=title, priority=priority, status='Pending')
        db.session.add(new_task)
        db.session.commit()
    return redirect(url_for('roadmap'))

@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    new_status = request.form.get('status')
    if new_status:
        task.status = new_status
        if new_status == 'Completed':
            task.progress_percentage = 100
        elif new_status == 'In Progress':
            task.progress_percentage = 50
        else:
            task.progress_percentage = 0
        db.session.commit()
    return redirect(url_for('roadmap'))

@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('roadmap'))

@app.route('/add_job', methods=['POST'])
def add_job():
    user = User.query.first()
    company = request.form.get('company')
    role = request.form.get('role')
    status = request.form.get('status')
    if company and role:
        new_job = JobApplication(
            user_id=user.id, 
            company=company, 
            role=role, 
            status=status,
            applied_date=datetime.now().date()
        )
        db.session.add(new_job)
        db.session.commit()
    return redirect(url_for('applications'))

@app.route('/delete_job/<int:job_id>', methods=['POST'])
def delete_job(job_id):
    job = JobApplication.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('applications'))

@app.route('/log_session', methods=['POST'])
def log_session():
    user = User.query.first()
    duration = request.form.get('duration', 25, type=int)
    new_session = StudySession(user_id=user.id, duration_minutes=duration, date=datetime.now().date())
    db.session.add(new_session)
    db.session.commit()
    return redirect(url_for('timer'))

@app.route('/chat', methods=['POST'])
def chat():
    user = User.query.first()
    user_msg_content = request.form.get('message')
    
    if not user_msg_content:
        return redirect(url_for('chatbot'))
        
    # Save user message
    user_msg = ChatMessage(user_id=user.id, role='user', content=user_msg_content)
    db.session.add(user_msg)
    db.session.commit()
    
    if not GEMINI_API_KEY or GEMINI_API_KEY == "your_api_key_here":
        # Fallback Mock Response
        ai_response_content = "I'm a mock AI response. Please add your actual Gemini API Key to the `.env` file to enable real intelligence!"
    else:
        try:
            # Construct history for context
            messages = ChatMessage.query.filter_by(user_id=user.id).order_by(ChatMessage.timestamp).all()
            history = []
            for msg in messages[:-1]: # exclude the latest one we just added
                role = "user" if msg.role == "user" else "model"
                history.append({"role": role, "parts": [msg.content]})
                
            model = genai.GenerativeModel('gemini-2.5-flash')
            chat_session = model.start_chat(history=history)
            response = chat_session.send_message(user_msg_content)
            ai_response_content = response.text
        except Exception as e:
            ai_response_content = f"Sorry, I encountered an error communicating with the API: {str(e)}"
            
    # Save AI response
    ai_msg = ChatMessage(user_id=user.id, role='ai', content=ai_response_content)
    db.session.add(ai_msg)
    db.session.commit()
    
    return redirect(url_for('chatbot'))

if __name__ == '__main__':
    app.run(debug=True)
