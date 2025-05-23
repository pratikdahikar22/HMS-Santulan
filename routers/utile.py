import os 
from fastapi import HTTPException
import jwt # type: ignore
from datetime import datetime, timedelta, timezone
from jwt import exceptions # type: ignore
# import time
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from typing_extensions import Annotated
from passlib.context import CryptContext # type: ignore
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


