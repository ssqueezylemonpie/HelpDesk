"""
Run this script once to create the database tables.
Usage: python run_schema.py
"""
from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

with open('schema.sql', 'r') as f:
    sql = f.read()

for statement in sql.strip().split(';'):
    statement = statement.strip()
    if statement:
        cursor.execute(statement)

conn.commit()
cursor.close()
conn.close()

print("Database tables created successfully!")
