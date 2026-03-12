# HRMS Lite Backend (FastAPI)

## Project Overview

This project provides the backend API for the HRMS Lite application. It allows administrators to manage employee records and track attendance through RESTful APIs.

## Features

* Add Employee
* View Employees
* Delete Employee
* Mark Attendance
* View Attendance Records

## Tech Stack

Backend: FastAPI (Python)
Database: MongoDB Atlas
Server: Uvicorn

## API Endpoints

Employees

POST /employees
Add a new employee

GET /employees
Fetch all employees

DELETE /employees/{employee_id}
Delete an employee

Attendance

POST /attendance
Mark attendance

GET /attendance/{employee_id}
Get attendance records

## Run Project Locally

Install dependencies

pip install -r requirements.txt

Run server

uvicorn main:app --reload

Server will start at

http://127.0.0.1:8000

API documentation available at

http://127.0.0.1:8000/docs

## Assumptions

* Single admin user
* No authentication implemented
* Basic employee and attendance management
