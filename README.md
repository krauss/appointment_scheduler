# Appointment Scheduler

## Overview
This simple scheduler allows you to either create a new appointment, or retrieve a list of appointments from an existing user.

## Usage
To create an appointment, do the following:

 - POST /api/appointment?user_id=`param1`&date=`param2`&time=`param3`

Where: 
 - `param1`: It's a user ID value. If it doesn't exist, the system creates it.
 - `param2`: It's a date value. It must be of the format YYY-MM-DD.
 - `param3`: It's a time value. It must be of the format HH:MM (secods are ignored).

To retrieve a list, do the following:

 - GET /api/appointments?user_id=`param1`

Where: 
 - `param1`: It's a user ID value. It must exists, otherwise the system will return an error.


## Build and Test

### To execute the API locally, follow the steps below:

1. 
```
git clone https://datahub-lab@dev.azure.com/datahub-lab/crawler/_git/mte-cnd
```
2. change directory.
```
cd tango_project
```
3. create a virtual environment.
```
python -m venv ve
```
4. activate it.
```
source ve/bin/activate
```
5. Install Python's dependencies.
```
pip3 install -r requirements.txt
```
6. Start the Uvicorn server
```
uvicorn server:app --host 0.0.0.0 
```
7. Open your browser and acess the URL: http://localhost:8000/