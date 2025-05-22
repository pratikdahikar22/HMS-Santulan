from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import user, patient, declaration_indemnity, medical_case_sheet1, medical_case_sheet2, periodic_checkup, declaration_consent_form, sexual_history, legal_history, referral, discharge_slip, high_risk_declaration, activity_sheet

app = FastAPI(
    title="Hospital Management(Santulan) API",
    description='''
        This API allows creating, updating, and retrieving Santulan Patient info.
    ''',
    version="1.1.0"
) 

# Allow all origins 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can also set specific origins like ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(user.router, tags=["Users"])
app.include_router(patient.router, tags=["Patient"])
app.include_router(medical_case_sheet1.router, tags=["Medical Case Sheet1"])
app.include_router(medical_case_sheet2.router, tags=["Medical Case Sheet2"])
app.include_router(periodic_checkup.router, tags=["Periodic Checkup Chart"])
app.include_router(declaration_indemnity.router, tags=["Declaration Cum Indemnity Form"])
app.include_router(declaration_consent_form.router, tags=["Consent And Declaration Form"])
app.include_router(high_risk_declaration.router)
app.include_router(sexual_history.router, tags=["Sexual History"])
app.include_router(legal_history.router, tags=["Legal History"])
app.include_router(referral.router, tags=["Referral"])
app.include_router(discharge_slip.router, tags=["Discharge Slip"])
app.include_router(activity_sheet.router, tags=["Activity Sheet"])




