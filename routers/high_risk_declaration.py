from fastapi import APIRouter
from models.high_risk_declaration import PersonalFamilyBackground, MaritalEducationalSocialHistory, HealthPsychologicalProfile
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import personal_family_background_collection, marital_educational_social_history_collection, health_psychological_profile_collection

router = APIRouter()



#-------------- Personal Family Background API (page-) -----------

@router.post("/personal-family-backgroud/", tags=["High Risk Declaration section 1"])
async def create_personal_family_backgroud(data: PersonalFamilyBackground):
    inserted_obj = personal_family_background_collection.insert_one(data.dict())
    
    return {
        "message": "Personal family background details submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/personal-family-backgroud/{patient_id}", tags=["High Risk Declaration section 1"])
async def get_personal_family_backgroud_by_patient_id(patient_id: str):
    try:
        obj = personal_family_background_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Personal family background details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Personal family background ID format")

@router.put("/personal-family-backgroud/{id}", tags=["High Risk Declaration section 1"])
async def update_personal_family_backgroud_by_id(id: str, updated_data:PersonalFamilyBackground):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Personal family background ID")

    result = personal_family_background_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Personal family background details not found")
    
    return {"message": "Personal family background details updated successfully"}


#-------------- Marital Educational Social History API (page-) -----------

@router.post("/marital-educational-social-history/", tags=["High Risk Declaration section 2"])
async def create_discharge_slip(data: MaritalEducationalSocialHistory):
    inserted_obj = marital_educational_social_history_collection.insert_one(data.dict())
    
    return {
        "message": "Histroy details submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/marital-educational-social-history/{patient_id}", tags=["High Risk Declaration section 2"])
async def get_discharge_slip_by_patient_id(patient_id: str):
    try:
        obj = marital_educational_social_history_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Histroy details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Histroy ID format")

@router.put("/marital-educational-social-history/{id}", tags=["High Risk Declaration section 2"])
async def update_discharge_slip_by_id(id: str, updated_data:MaritalEducationalSocialHistory):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Histroy ID")

    result = marital_educational_social_history_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Histroy details not found")
    
    return {"message": "Histroy details updated successfully"}



#-------------- Health psychological profile API (page-15) -----------

@router.post("/health-psychological-profile/", tags=["High Risk Declaration section 3"])
async def create_health_psychological_profile(data: HealthPsychologicalProfile):
    inserted_obj = health_psychological_profile_collection.insert_one(data.dict())
    
    return {
        "message": "Profile details submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/health-psychological-profile/{patient_id}", tags=["High Risk Declaration section 3"])
async def get_health_psychological_profile_by_patient_id(patient_id: str):
    try:
        obj = health_psychological_profile_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Profile details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Profile ID format")

@router.put("/health-psychological-profile/{id}", tags=["High Risk Declaration section 3"])
async def update_health_psychological_profile_by_id(id: str, updated_data: HealthPsychologicalProfile):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Profile ID")

    result = health_psychological_profile_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Profile details not found")
    
    return {"message": "Profile details updated successfully"}





