
import sqlite3
from app.models import Activity

def add(activity: Activity):
    # Connect to the SQLite database
    conn = sqlite3.connect('activities.db')
    cursor = conn.cursor()

    # Create the activities table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS activities
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       timestamp INTEGER,
                       amount INTEGER,
                       user_id INTEGER
                       )''')

    # Insert the activity into the database
    cursor.execute('''INSERT INTO activities (name, timestamp, amount, user_id)
                      VALUES (?, ?, ?, ?)''',
                   (activity.name, activity.timestamp, activity.amount, activity.user_id))
    activity_id = cursor.lastrowid

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Return the ID of the inserted activity
    return activity_id

def get_total_number_of_pushups(user_id: int) -> int:
    activity_name = "pushups"
    raise NotImplemented
