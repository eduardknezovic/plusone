import random

from typing import List

from app.models.activity import Activity 
from app.crud import get_all_user_activity

def get_response_for_successful_updating_of_activity(activity: Activity) -> str:
    message = "+{} {}!".format(activity.amount, activity.name, activity.user_id)
    message += "\n\n"
    message += "You've completed a total of {} {}. Keep going!".format(get_activity_sum(activity.user_id, activity.name), activity.name)
    message += "\n\n"
    message += get_customized_message(activity)
    return message

def get_activity_sum(user_id: int, activity_name: str) -> int:
    activities: List[Activity] = get_all_user_activity(user_id)
    total = 0
    for activity in activities:
        if activity.name == activity_name:
            total += activity.amount
    return total

def get_customized_message(activity: Activity = None) -> str: # "activity" is an optional parameter
    messages = [
        "Embrace the grind and outwork your competition.",
        "Failure is just a stepping stone on the path to success.",
        "Take control of your life and seize every opportunity.",
        "Don't wait for the perfect moment; create it.",
        "Invest in yourself and become the best version of you.",
        "Chase your dreams with unapologetic passion and determination.",
        "Your mindset determines your outcome; cultivate a winning mentality.",
        "Rise above the noise and negativity; focus on your goals and let nothing stop you."
    ]
    inp = random.randint(0,int(len(messages) - 1))
    return messages[inp]