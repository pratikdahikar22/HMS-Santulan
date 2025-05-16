from pydantic import BaseModel
from typing import Optional, List


# -------------Periodically Checkup Chart page-4 --------------

class PatientInfo(BaseModel):
    name: str
    age: str
    month: str
    year: str
    registration_no: str
    diagnosis: str

class BPChartEntry(BaseModel):
    date: str
    time: str
    bp: str
    pulse: str
    medication: str

class HourlyReading(BaseModel):
    hour: str
    temperature_f: str
    bp: str
    pulse: str

class TemperatureChartEntry(BaseModel):
    date: str
    hourly_readings: List[HourlyReading]

class WeightChartEntry(BaseModel):
    date: str
    weight: str

class PeriodicCheckupChart(BaseModel):
    patient_id: str
    patient_info: PatientInfo
    bp_chart: List[BPChartEntry]
    temperature_chart: List[TemperatureChartEntry]
    weight_chart: List[WeightChartEntry]

