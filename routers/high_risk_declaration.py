from fastapi import APIRouter
from models.high_risk_declaration import HighRiskDeclarationForm, FamilyHistoryForm, ChildhoodAndAdolescent, PatientHistory, FamilyHealthStatus
from typing import Optional, List
from bson import ObjectId     # type: ignore
from bson.errors import InvalidId # type: ignore
from fastapi import HTTPException
from db import high_risk_declaration_form_collection, family_history_form_collection, childhood_and_adolescent_collection, patient_history_collection, family_health_status_collection
from .utile import verify_token




router = APIRouter(
    # dependencies=[Depends(verify_token)]
)



# ------------------- Section 1 -------------------

@router.post("/high-risk-declaration/", tags=["High Risk Declaration section 1"])
async def create_high_risk_declaration(data: HighRiskDeclarationForm):
    inserted_obj = high_risk_declaration_form_collection.insert_one(data.dict())
    
    return {
        "message": "High Risk Declaration section 1 submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/high-risk-declaration/{patient_id}", tags=["High Risk Declaration section 1"])
async def get_high_risk_declaration_by_patient_id(patient_id: str):
    try:
        obj = high_risk_declaration_form_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Patient details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

@router.put("/high-risk-declaration/{id}", tags=["High Risk Declaration section 1"])
async def update_high_risk_declaration_by_id(id: str, updated_data: HighRiskDeclarationForm):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID")

    result = high_risk_declaration_form_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Patient details not found")
    
    return {"message": "High Risk Declaration details updated successfully"}


# ------------------- Section 2 -------------------

@router.post("/family-history-form/", tags=["High Risk Declaration section 2"])
async def create_family_history_form(data: FamilyHistoryForm):
    inserted_obj = family_history_form_collection.insert_one(data.dict())
    
    return {
        "message": "Family history details submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/family-history-form/{patient_id}", tags=["High Risk Declaration section 2"])
async def get_family_history_form_by_patient_id(patient_id: str):
    try:
        obj = family_history_form_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Family history details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Family history ID format")

@router.put("/family-history-form/{id}", tags=["High Risk Declaration section 2"])
async def update_family_history_form_by_id(id: str, updated_data:FamilyHistoryForm):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Family history ID")

    result = family_history_form_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Family history details not found")
    
    return {"message": "Family history details updated successfully"}

# ------------------- Section 3 -------------------

@router.post("/childhood-adolescent/", tags=["High Risk Declaration section 3"])
async def create_childhood_adolescent(data: ChildhoodAndAdolescent):
    inserted_obj = childhood_and_adolescent_collection.insert_one(data.dict())
    
    return {
        "message": "Childhood and Adolescent details submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/childhood-adolescent/{patient_id}", tags=["High Risk Declaration section 3"])
async def get_childhood_adolescent_by_patient_id(patient_id: str):
    try:
        obj = childhood_and_adolescent_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Childhood and Adolescent details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

@router.put("/childhood-adolescent/{id}", tags=["High Risk Declaration section 3"])
async def update_childhood_adolescent_by_id(id: str, updated_data:ChildhoodAndAdolescent):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Childhood and Adolescent ID")

    result = childhood_and_adolescent_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Childhood and Adolescent details not found")
    
    return {"message": "Childhood and Adolescent details updated successfully"}


# ------------------- Section 4 -------------------

@router.post("/patient-history/", tags=["High Risk Declaration section 4"])
async def create_patient_history(data: PatientHistory):
    inserted_obj = patient_history_collection.insert_one(data.dict())
    
    return {
        "message": "Patient History details submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/patient-history/{patient_id}", tags=["High Risk Declaration section 4"])
async def get_patient_history_by_patient_id(patient_id: str):
    try:
        obj = patient_history_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Patient History details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

@router.put("/patient-history/{id}", tags=["High Risk Declaration section 4"])
async def update_patient_history_by_id(id: str, updated_data:PatientHistory):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Patient History ID")

    result = patient_history_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Patient History details not found")
    
    return {"message": "Patient History details updated successfully"}


# ------------------- Section 5 -------------------

@router.post("/family-health-status/", tags=["High Risk Declaration section 5"])
async def create_family_health_status(data: FamilyHealthStatus):
    inserted_obj = family_health_status_collection.insert_one(data.dict())
    
    return {
        "message": "Family health status details submitted successfully",
        "id": str(inserted_obj.inserted_id)
    }

@router.get("/family-health-status/{patient_id}", tags=["High Risk Declaration section 5"])
async def get_family_health_status_by_patient_id(patient_id: str):
    try:
        obj = family_health_status_collection.find_one({"patient_id": patient_id})
        if not obj:
            raise HTTPException(status_code=404, detail="Family health status details not found")
        
        # Convert ObjectId to string
        obj["id"] = str(obj["_id"])
        del obj["_id"]

        return obj

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

@router.put("/family-health-status/{id}", tags=["High Risk Declaration section 5"])
async def update_family_health_status_by_id(id: str, updated_data:FamilyHealthStatus):
    try:
        obj_id = ObjectId(id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid Family health status ID")

    result = family_health_status_collection.update_one(
        {"_id": obj_id},
        {"$set": updated_data.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Family health status details not found")
    
    return {"message": "Family health status details updated successfully"}









