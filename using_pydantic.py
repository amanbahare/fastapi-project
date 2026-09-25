from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Optional, Dict, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(max_length=10, title="Patient Name", description="Please provide your name under 10 word")]
    age : int 
    email : EmailStr
    linkedIn_URL : AnyUrl 
    weight : Annotated[float, Field(gt=0, lt=400, strict=True)] # strict = true means cant provide string [ if we dont use strict we can provide string float value pydantic automatically handle it and convert it to float or int]
    married : Optional[bool] = None
    allergies : Annotated[List[str],Field(max_length=5, default=None)]
    contact : Optional[Dict[str, str]] = None

patient_info = {"name": "Aman", "age": '27', "email": "amanbahare99@gmail.com","linkedIn_URL": "https://chat.deepseek.com/", 
                "weight": 62.5, "allergies": ["polen", "dust"], "contact": {"email": "@ggndcom", "phone": "808500916"} }

p1 = Patient(**patient_info)

def insert_patient_data(p1 : Patient):
    print(p1.name)
    print(p1.age)
    print("data inserted")

def update_patient_data(p1 : Patient):
    print(p1.name)
    print(p1.age)
    print(p1.email)
    print(p1.linkedIn_URL)
    print(p1.weight)
    print(p1.married)
    print(p1.allergies)
    print(p1.contact)
    print("data updated")

update_patient_data(p1)