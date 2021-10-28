# stdlib imports
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta

# 3rd party imports
from fastapi import HTTPException

@dataclass
class Appointment:

    appointment_id: str
    user_id: str
    date: str
    start_datetime: str
    end_datetime: str

class Scheduler:

    def __init__(self) -> None:
        self.appointment_list = {}

    async def create_appointment(self, user_id: str, date: str, time: str):
        user = self.appointment_list.get(user_id)

        # If it's a new user
        if not user:
            if time.split(':')[1] != '00' and time.split(':')[1] != '30':
                raise HTTPException(status_code=400, detail="Appointments can only be created at minutes 00 or 30.")

            start_dt = datetime.fromisoformat(f'{date} {time}:00')
            end_dt = start_dt + timedelta(minutes=30)

            appointment = Appointment(str(uuid.uuid1()), user_id, date, str(start_dt), str(end_dt))

            self.appointment_list[user_id] = {"appointments": [appointment]}
            return appointment

        # If it's an existing user
        else:
            user_appointment_list = self.appointment_list.get(user_id).get('appointments')

            # Checks if the user doesn't already have an appointment on that day
            day = date.split('/')[-1]
            for apntmt in user_appointment_list:
                if apntmt.start_datetime.split()[0].split('/')[-1] == day:
                    raise HTTPException(status_code=400, detail="You can only have one appointment per day.")
            
            # All good, he can have his appointment.
            start_dt = datetime.fromisoformat(f'{date} {time}:00')
            end_dt = start_dt + timedelta(minutes=30)

            app_id = str(uuid.uuid1()).split('-')[0] # A shorter ID looks better
            appointment = Appointment(app_id, user_id, date, str(start_dt), str(end_dt))

            user_appointment_list.append(appointment)

            return appointment


    async def get_appointments(self, user_id: str):
        user = self.appointment_list.get(user_id)

        if user:
            return user.get("appointments")
        else:
            raise HTTPException(status_code=400, detail="User not found.")