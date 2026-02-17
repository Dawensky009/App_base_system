from sqlalchemy.exc import SQLAlchemyError
from database import SessionLocal
from models.user import User

def debug_insert():
    print("Starting debug insertion...")
    db = SessionLocal()
    try:
        # Check if user already exists
        message = "Debugging insertion..."
        print(message)
        
        email = "debug_test@example.com"
        existing = db.query(User).filter(User.email == email).first()
        if existing:
            print(f"User {email} already exists. Deleting for test...")
            db.delete(existing)
            db.commit()
            print("Deleted existing user.")

        # Attempt insertion
        new_user = User(
            username="debug_user",
            email=email,
            hashed_password="hashed_secret",
            role="admin"
        )
        print("Attempting add...")
        db.add(new_user)
        print("Attempting commit...")
        db.commit()
        print("Attempting refresh...")
        db.refresh(new_user)
        
        print(f"Insertion SUCCESSFUL! User ID: {new_user.id}")
        
    except SQLAlchemyError as e:
        db.rollback()
        print(f"SQLAlchemy Error: {str(e)}")
    except Exception as e:
        db.rollback()
        print(f"General Error: {str(e)}")
    finally:
        db.close()
        print("End of debug script.")

if __name__ == "__main__":
    debug_insert()
