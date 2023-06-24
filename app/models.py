
from pydantic import BaseModel

class Activity(BaseModel):
    user_id: int
    name: str
    amount: int
    timestamp: int

def get_activity_from_telegram_message(message):
    command_parts = message.text.split()
    if len(command_parts) == 2:
        name = command_parts[0][1:]  # Remove the slash "/" character
        amount = int(command_parts[1])
        user_id = message.chat.id
        if name == "pushup":
            name = "pushups" # Standardize the activity name
        return Activity(user_id=user_id, name=name, amount=amount, timestamp=message.date)
    else:
        return None
