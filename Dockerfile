FROM python:3.9-slim-buster

LABEL name="appointment_scheduler"

LABEL version="1.0"

WORKDIR /usr/src/app

COPY . .

RUN pip3 install --quiet -r requirements.txt

EXPOSE 80/tcp

CMD [ "uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80" ]
