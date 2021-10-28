# 3rd party imports
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Query

# Local imports
from src import api, models

#---------------------------- Application -------------------------------
app = FastAPI(
    title='Appointment Scheduler - REST API', 
    description="Appointment Scheduler", 
    debug=False
)
scheduler = api.Scheduler()

#---------------------------- Query params -------------------------------
# Date validator
date_validator = Query(
    ...,
    description='Calendar date in the format: YYYY-MM-DD', 
    min_length=10, 
    max_length=10
)

# Time validator
time_validator = Query(
    ...,
    description='Time in HH:MM format, with 00:00 being midnight and 13:30 being 1:30 PM',
    min_length=5, 
    max_length=5,
    regex='[0-2][0-9]:[0-5][0-9]'
)

# User ID validator
user_validator = Query(
    ...,
    description='User ID that contains only letters, digits and underscore (_)', 
    regex="\w+"
)

#---------------------------- Endpoints -------------------------------
@app.post("/api/appointment", response_model=models.Appointment)
async def create_appointment(date: str = date_validator, time: str= time_validator ,user_id: str = user_validator):    
    return await scheduler.create_appointment(user_id, date, time)

@app.get("/api/appointments")
async def get_appointment_list(user_id: str = user_validator):
    return await scheduler.get_appointments(user_id)

#---------------------------- Static Files -------------------------------
app.mount("/", StaticFiles(directory="static", html=True), name="static")