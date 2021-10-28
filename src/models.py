from typing import  Optional
from pydantic import BaseModel

class Appointment(BaseModel):    
    appointment_id: str
    user_id: str
    date: str
    start_datetime: str
    end_datetime: str