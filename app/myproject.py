from fastapi import FastAPI,Body
from pydantic import BaseModel
import csv
import bcrypt

app = FastAPI()

header = ['name','password','age']

class Student(BaseModel): 
    name:str 
    password:str
    age:int



@app.get("/")
def index():

    return {"name":"seidu"}


@app.post("/create")
def signup(data=Body()):
    password=data['password']
    #encrypting the password
    password=password.encode('utf-8')
    hashedpwd = bcrypt.hashpw(password,bcrypt.gensalt())
    #replacing the password with encrypted password
    data['password']=hashedpwd
    #reading the files into the csv file
    with open('data.csv','a',newline='') as f:
        writer = csv.DictWriter(f,fieldnames=header)
        writer.writeheader()
        writer.writerow(data)
    return data