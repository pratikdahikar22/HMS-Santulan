from fastapi import APIRouter
from models.declaration_indemnity import DeclarationIndemnityForm
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import declaration_indemnity_form_collection

router = APIRouter()

# declaration_indemnity_form_collection = database['declarationIndemnityForm']


#-------------- Declaration cum indemnity form API -----------

@router.post("/declaration-form/")
async def create_declaration_form(form_data: DeclarationIndemnityForm):
    decliaration_form_data = declaration_indemnity_form_collection.insert_one(form_data.dict())
    
    return {
        "message": "Declaration form submitted successfully",
        "submitted_data": str(decliaration_form_data.inserted_id)
    }

@router.get("/declaration-form/{user_id}")
async def get_declaration_form_by_userId(user_id: str):
    try:
        declaration_form_obj = declaration_indemnity_form_collection.find_one({"user_id": user_id})
        if not declaration_form_obj:
            raise HTTPException(status_code=404, detail="declaration form not found")
        
        # Convert ObjectId to string
        declaration_form_obj["id"] = str(declaration_form_obj["_id"])
        del declaration_form_obj["_id"]

        return declaration_form_obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid form ID format")

@router.put("/declaration-form/{id}")
async def update_declaration_form_by_id(id: str, updated_data: dict):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid declaration form  ID")

    result = declaration_indemnity_form_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="declaration form  not found")
    
    return {"message": "Declaration form updated successfully"}

