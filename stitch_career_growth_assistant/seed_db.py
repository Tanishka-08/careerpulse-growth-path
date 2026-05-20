from models import db, User, JobApplication, Event, Task, StudySession
from datetime import datetime, timedelta, date

def seed_database(app_instance=None, drop_existing=True):
    if app_instance is None:
        from app import app as app_instance
        
    with app_instance.app_context():
        if drop_existing:
            # Clear existing data
            db.drop_all()
            db.create_all()
        else:
            db.create_all()

        # 1. Create User
        user1 = User(
            name="Alex Rivers",
            email="alex@example.com",
            velocity_score=82
        )
        db.session.add(user1)
        db.session.commit()

        # 2. Job Applications
        job1 = JobApplication(
            user_id=user1.id,
            company="NexGen AI",
            role="Senior Platform Engineer",
            status="Technical Interview",
            applied_date=date(2023, 10, 24)
        )
        job2 = JobApplication(
            user_id=user1.id,
            company="Stellar SaaS",
            role="Staff Architect",
            status="Offer Extended",
            applied_date=date(2023, 10, 22)
        )
        job3 = JobApplication(
            user_id=user1.id,
            company="Vortex FinTech",
            role="Lead Backend dev",
            status="Applied",
            applied_date=date(2023, 10, 20)
        )
        db.session.add_all([job1, job2, job3])

        # 3. Tasks
        task1 = Task(
            user_id=user1.id,
            title="System Design Mastery: Complete Section 4",
            progress_percentage=0,
            status="Pending",
            priority=1
        )
        task2 = Task(
            user_id=user1.id,
            title="Portfolio Update: Draft case study",
            progress_percentage=0,
            status="Scheduled",
            priority=2
        )
        task3 = Task(
            user_id=user1.id,
            title="Morning Skill Drill: 3 Leetcode Medium",
            progress_percentage=100,
            status="Completed",
            priority=1
        )
        db.session.add_all([task1, task2, task3])

        # 4. Events
        now = datetime.now()
        event1 = Event(
            user_id=user1.id,
            title="System Design Study",
            event_type="Study",
            start_time=now + timedelta(days=2, hours=10)
        )
        event2 = Event(
            user_id=user1.id,
            title="Mock Interview",
            event_type="Interview",
            start_time=now + timedelta(days=3, hours=14),
            end_time=now + timedelta(days=3, hours=15, minutes=30)
        )
        event3 = Event(
            user_id=user1.id,
            title="Google Resume DL",
            event_type="Deadline",
            start_time=now + timedelta(days=4, hours=23, minutes=59)
        )
        db.session.add_all([event1, event2, event3])

        # 5. Study Sessions
        session1 = StudySession(
            user_id=user1.id,
            duration_minutes=120,
            date=now.date()
        )
        session2 = StudySession(
            user_id=user1.id,
            duration_minutes=150,
            date=now.date() - timedelta(days=1)
        )
        db.session.add_all([session1, session2])

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
