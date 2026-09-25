from pydantic import BaseModel, EmailStr, AnyUrl, field_validator
from typing import List, Optional, Dict

class Patient(BaseModel):
    name : str 
    age : int 
    email : EmailStr
    linkedIn_URL : AnyUrl
    weight : float 
    married : Optional[bool] = None
    allergies : Optional[List[str]] = None
    contact : Optional[Dict[str, str]] = None

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']

        domain = value.split('@')[-1]

        if domain not in valid_domains:
            raise ValueError(f"please enter valid domain from {valid_domains}")
        return value

    @field_validator('name')
    @classmethod 
    def upper_name(cls, value):
        return value.upper()

patient_info = {"name": "Aman", "age": '27', "email": "amanbahare99@hdfc.com","linkedIn_URL": "https://chat.deepseek.com/", 
                "weight": 62, "allergies": ["polen", "dust"], "contact": {"email": "@ggndcom", "phone": "808500916"} }

p1 = Patient(**patient_info)

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