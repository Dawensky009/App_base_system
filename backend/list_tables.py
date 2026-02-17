from sqlalchemy import inspect
from database import engine

def list_tables():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("Existing Tables:")
    for table in tables:
        print(f" - {table}")
    
    if "users" in tables:
        print("\nSUCCESS: 'users' table FOUND.")
    else:
        print("\nFAILURE: 'users' table NOT FOUND.")

if __name__ == "__main__":
    list_tables()
