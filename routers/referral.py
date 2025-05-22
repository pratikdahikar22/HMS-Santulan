from fastapi import APIRouter
from models.referral import ReferralAndTreatmentModel
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import referral_collection

from fastapi import APIRouter, Depends
from .utile import verify_token
from .utile import verify_token



router = APIRouter(
    # dependencies=[Depends(verify_token)]
)



#-------------- Referral API (page-14) -----------

@router.post("/referral/")
async def create_referral(data: ReferralAndTreatmentModel):
    inserted_obj = referral_collection.insert_one(data.dict())
    
    return {
        "message": "Referral details submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/referral/{patient_id}")
async def get_referral_by_patient_id(patient_id: str):
    try:
        obj = referral_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Referral details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Referral ID format")

@router.put("/referral/{id}")
async def update_referral_by_id(id: str, updated_data:ReferralAndTreatmentModel):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Referral ID")

    result = referral_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Referral details not found")
    
    return {"message": "Referral details updated successfully"}


