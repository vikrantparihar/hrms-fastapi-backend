from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = MongoClient("mongodb://admin:Admin12345@ac-rmwwhfx-shard-00-00.fzdoegh.mongodb.net:27017,ac-rmwwhfx-shard-00-01.fzdoegh.mongodb.net:27017,ac-rmwwhfx-shard-00-02.fzdoegh.mongodb.net:27017/?ssl=true&replicaSet=atlas-lbybwq-shard-0&authSource=admin&appName=Cluster0")

db = client.hrms
employees = db.employees


class Employee(BaseModel):
    employee_id: str
    name: str
    email: str
    department: str


@app.get("/")
def home():
    return {"message": "HRMS API Running"}


@app.post("/employees")
def add_employee(emp: Employee):
    employees.insert_one(emp.dict())
    return {"message": "Employee added"}


@app.get("/employees")
def get_employees():
    data = []
    for emp in employees.find():
        emp["_id"] = str(emp["_id"])
        data.append(emp)
    return data


class Attendance(BaseModel):
    employee_id: str
    date: str
    status: str


attendance = db.attendance


@app.post("/attendance")
def mark_attendance(att: Attendance):
    attendance.insert_one(att.dict())
    return {"message": "Attendance marked"}


@app.get("/attendance")
def get_attendance():

    data = []

    for att in attendance.find():
        att["_id"] = str(att["_id"])
        data.append(att)

    return data