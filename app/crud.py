
import sqlite3
from models import Activity
from datetime import datetime

def add(activity: Activity):
    # Connect to the SQLite database
    conn = sqlite3.connect('activities.db')
    cursor = conn.cursor()

    # Create the activities table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS activities
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       timestamp INTEGER,
                       amount INTEGER)''')

    # Insert the activity into the database
    cursor.execute('''INSERT INTO activities (name, date, amount)
                      VALUES (?, ?, ?)''',
                   (activity.name, activity.timestamp, activity.amount))
    activity_id = cursor.lastrowid

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Return the ID of the inserted activity
    return activity_id
