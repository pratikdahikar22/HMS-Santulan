from pydantic import BaseModel, EmailStr, validator
from typing import Optional,Literal

class User(BaseModel):
    firstName: str
    lastName: str
    username: str
    password: str
    role: Literal["Admin", "Doctor"]
    email: EmailStr

class GetUser(BaseModel):
    firstName: str
    lastName: str
    username: str
    # password: str
    role: Literal["Admin", "Doctor"]
    email: EmailStr
    
class Login(BaseModel):
    username: str
    password: str
