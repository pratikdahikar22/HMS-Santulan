import os
from pymongo import MongoClient    #type: ignore
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


url = os.getenv("DATABASE_URL")
client = MongoClient(url)
database = client.get_database()


users_collection   = database['users']
patient_collection = database['patient']
periodic_checkup_collection           = database['PeriodicCheckup']
declaration_consent_collection        = database['declarationConsentForm']
declaration_indemnity_form_collection = database['declarationIndemnityForm']
drinking_drug_history_collection      = database['drinkingDrugHistory']
medical_case_sheet2_collection        = database['medicalCaseSheet2']
sexual_histroy_collection             = database['sexualHistory']
legal_histroy_collection              = database['legalHistory']
referral_collection                   = database['referral']
discharge_slip_collection             = database['dischargeSlip']
activity_sheet_collection             = database['activitySheet']

# high_risk_declaration_collection
high_risk_declaration_form_collection = database['highRiskDeclarationForm']
family_history_form_collection = database['familyHistoryForm']
childhood_and_adolescent_collection = database['childhoodAndAdolescent']
patient_history_collection = database['patientHistory']
family_health_status_collection = database['familyHealthStatus']



