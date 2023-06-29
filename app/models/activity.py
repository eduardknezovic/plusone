
from pydantic import BaseModel

class Activity(BaseModel):
    user_id: int
    name: str
    amount: int
    timestamp: int

