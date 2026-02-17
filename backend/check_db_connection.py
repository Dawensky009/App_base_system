from sqlalchemy import text
from database import engine

def check_db_connection():
    try:
        # Use a connection to execute a simple query
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("SUCCESS: Successfully connected to the database!")
            for row in result:
                print(f"Query Result: {row[0]}")
    except Exception as e:
        print(f"ERROR: Failed to connect to the database: {e}")

if __name__ == "__main__":
    check_db_connection()
