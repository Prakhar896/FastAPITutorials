from typing import Annotated
from fastapi import FastAPI, Depends

app = FastAPI()

class Logger:
    def log(self, message: str):
        print(f"Log entry: {message}")

class EmailService:
    def send_email(self, recipient: str, message: str):
        print(f"Sending email to {recipient}: {message}")

def get_logger():
    return Logger()

def get_email_service():
    return EmailService()

logger_dependency = Annotated[Logger, Depends(get_logger)]
email_service_dependency = Annotated[EmailService, Depends(get_email_service)]

@app.get('/log/{message}')
def log_message(message: str, logger: logger_dependency):
    logger.log(message)
    
    return message

@app.get('/email/{recipient}/{message}')
def send_email(recipient: str, message: str, email_service: email_service_dependency):
    email_service.send_email(recipient, message)
    
    return {"recipient": recipient, "message": message}