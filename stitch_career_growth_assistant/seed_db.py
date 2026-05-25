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

        # 2. Job Applications (No default applications seeded)
        # Starting with a fresh, empty job application list
        pass

        # 3. Tasks (Starting with a fresh, empty task list for the user)
        # No tasks seeded by default


        # 4. Events (No default events seeded)
        # Starting with a fresh, empty calendar list
        pass

        # 5. Study Sessions
        # Starting with a fresh, empty study session list
        pass

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
