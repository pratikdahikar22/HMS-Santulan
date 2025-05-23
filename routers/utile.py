import os 
from fastapi import HTTPException, Depends
import jwt # type: ignore
from jwt import exceptions # type: ignore
from datetime import datetime, timedelta, timezone
# import time
from fastapi.security import OAuth2PasswordBearer
# from fastapi import Depends
from typing_extensions import Annotated
from passlib.context import CryptContext # type: ignore

# email import
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()


SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM  = os.getenv('ALGORITHM')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context   = CryptContext(schemes=["bcrypt"], deprecated="auto")



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(days=int(os.getenv('REFRESH_TOKEN_EXPIRE_DAYS')))
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: Annotated[str, Depends(oauth2_scheme)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print(payload)
        username: str = payload.get("username")
        if username is None:
            raise ValueError("Invalid token: subject missing")
        return payload  # or username
    except exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except exceptions.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")



# sent email 
def send_email(receiver_email, subject, html_content):
    sender_email = os.getenv('SENDER_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')  

    # Create MIME message
    msg = MIMEMultipart("alternative")
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    # Attach the HTML content
    html_part = MIMEText(html_content, "html")
    msg.attach(html_part)

    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        return {
        'statusCode': 200, 
        'message': "Email sent successfully!"
        }
    except Exception as e:
        print("Failed to send_email:", e)
        return {
        'statusCode': 400, 
        'message': "Failed to send email!"
        }


