import sqlite3
import shutil
import os
import datetime

def init_database():
    db_name = 'dentalscheduler.db'
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f'dentalschedulerBU_{timestamp}.db'
    
    #Check if db exists
    if os.path.exists(db_name):
        print(f'Backing up {db_name} to {backup_name}...')
        shutil.copy(db_name, backup_name)
        print('Backup completed!')
    else:
        print(f'No existing database found. Skipping backup.')

    #Connect to the database
    connection = sqlite3.connect("dentalscheduler.db")
    cursor = connection.cursor()

    #Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        consent INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS procedures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        duration INTEGER NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        procedure_id INTEGER,
        appointment_time TEXT NOT NULL,
        FOREIGN KEY (patient_id) REFERENCES patients(id),
        FOREIGN KEY (procedure_id) REFERENCES procedures(id)
    )
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    init_database()