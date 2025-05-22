from fastapi import APIRouter,Depends
from models.declaration_consent_form import DeclarationConsentForm 
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import declaration_consent_collection
from .utile import verify_token


router = APIRouter(
    # dependencies=[Depends(verify_token)]
)


# declaration_consent_collection = database['declarationConsentForm']


#-------------- Declaration Consent Form API (page-6,7) -----------

@router.post("/declaration-consent-form/")
async def create_declaration_consent_form(data: DeclarationConsentForm):
    inserted_obj = declaration_consent_collection.insert_one(data.dict())
    
    return {
        "message": "Consent Form submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/declaration-consent-form/{patient_id}")
async def get_declaration_consent_form_by_patient_id(patient_id: str):
    try:
        obj = declaration_consent_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Consent form not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid consent ID format")

@router.put("/declaration-consent-form/{id}")
async def update_declaration_consent_form_by_id(id: str, updated_data:DeclarationConsentForm):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Cosent ID")

    result = declaration_consent_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Consent form not found")
    
    return {"message": "Consent form updated successfully"}


