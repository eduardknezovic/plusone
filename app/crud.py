
from typing import List

import sqlite3

from app.models.activity import Activity

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

def get_all_user_activity(user_id: int) -> List[Activity]:
    # Connect to the SQLite database
    conn = sqlite3.connect('activities.db')
    cursor = conn.cursor()

    # Retrieve all activities for the given user_id
    cursor.execute('SELECT id, name, timestamp, amount, user_id FROM activities WHERE user_id = ?', (user_id,))
    result_set = cursor.fetchall()

    # Process the retrieved data and create a list of Activity objects
    activities = []
    for row in result_set:
        activity = Activity(
            id=row[0],
            name=row[1],
            timestamp=row[2],
            amount=row[3],
            user_id=row[4]
        )
        activities.append(activity)

    # Close the database connection
    conn.close()

    # Return the list of Activity objects
    return activities

