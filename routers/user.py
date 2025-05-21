from fastapi import APIRouter, Request
from models.user import User, GetUser, FogotPassword
from db import users_collection
from fastapi.security import OAuth2PasswordRequestForm
from typing_extensions import Annotated
from fastapi import FastAPI, Header, Depends, HTTPException
from datetime import datetime, timedelta
from .utile import create_access_token, create_refresh_token, verify_token, pwd_context, SECRET_KEY, ALGORITHM
from bson import ObjectId  # type: ignore
from typing import List
import jwt # type: ignore
from bson.errors import InvalidId # type: ignore


router = APIRouter()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def update_user_info(res):
    res['id'] = str(res['_id'])
    del res["_id"]
    # del res["password"]
    return res

@router.get("/")
def home(decrypted_data:dict=Depends(verify_token)):
    return {"message": "Home Page..!"}
    
@router.post("/login/")
async def user_login(login_info: Annotated[OAuth2PasswordRequestForm, Depends()]):
    username = login_info.username
    password = login_info.password

    resp = {}
    try:
        if username=='' or password=='': raise  HTTPException(status_code=400, detail='username and password required ..!')

        user = users_collection.find_one({"username": username})
        
        if user == None: raise HTTPException(status_code=400, detail='Invalid username...!')
        
        
        if verify_password(password, user['password']):
            data = {
                'id': str(user['_id']),
                'username': user['username'],
                'role': user['role'],
                'firstName': user.get('firstName'),
                'lastName': user.get('lastName'),
                'email': user.get('email'),
            }
            access_token = create_access_token(data=data)
            refresh_token = create_refresh_token(data=data)
            
            resp = {
               'user_info': data,
               'access_token': access_token,
               'refresh_token': refresh_token 
            }            
            
            return resp

        else: raise HTTPException(status_code=400, detail="Invalid password..!")
        
    except Exception as e:
        print('user login error: ', str(e))
        raise HTTPException(status_code=400, detail=str(e.detail))    

@router.post("/refresh")
def refresh_token(request: Request):
    auth_header = request.headers.get("Authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    
    refresh_token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        # print(payload)
        if payload.get("type") != "refresh":
            raise HTTPException(status_code=401, detail="Invalid token type")
        username = payload.get("username")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    new_access_token = create_access_token(payload)
    return {"access_token": new_access_token}


@router.post("/forgot-password/")
async def forgot_password(user_info:FogotPassword, decrypted_data:dict=Depends(verify_token)):
    print(decrypted_data) 
    role = decrypted_data.get('role','')
    user_info = user_info.dict()
    user_id = user_info.get('userId','')
    new_password = user_info.get('newPassword','')
    
    if role != "Admin":
        raise HTTPException(status_code=400, detail='Unathorize (Only Admin has permission to this API)')
    
    # user = users_collection.find({'_id': ObjectId(user_id)})

    try:
        obj_id = ObjectId(user_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail='Invalid user Id...!')

    result = users_collection.update_one(
        {'_id': obj_id},
        {'$set': {'password': hash_password(new_password)}}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=400, detail='User not found')
    
    return {
        'message': "User password change successfully..!"
    }



@router.post("/user/")
async def create_user(user_data: User, decrypted_data:dict=Depends(verify_token)):

    if decrypted_data.get('role','') != 'Admin': 
        raise HTTPException(status_code=401, detail='Only Admin can create user')
    
    data = user_data.dict()
    
    username = data.get('username')
    password = data.get('password')
    if username=='' or password=='': raise  HTTPException(status_code=400, detail='username and password required ..!')
    
    # Check user already exist
    user = users_collection.find_one({'username': data.get('username')})
    if user:
        raise HTTPException(status_code=400, detail='User with this username already exist..!')
    
    
    data['password'] = hash_password(password)
    data['created_at'] = datetime.now()
    data['updated_at'] = datetime.now()
    
    res = users_collection.insert_one(data)

    return {
        'message': 'user created successfully',  
        'user_id': str(res.inserted_id)
    }

@router.get("/user/", response_model=List[GetUser])
async def get_all_users(decrypted_data:dict=Depends(verify_token)):
    results = users_collection.find().sort('firstName')
    results = list(map(update_user_info, results))
    return results



