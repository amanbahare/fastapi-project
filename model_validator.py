from pydantic import BaseModel, EmailStr, AnyUrl, model_validator
from typing import List, Optional, Dict

class Patient(BaseModel):
    name : str 
    age : int 
    email : EmailStr
    linkedIn_URL : AnyUrl
    weight : float 
    married : Optional[bool] = None
    allergies : Optional[List[str]] = None
    contact : Dict[str, str]

    @model_validator(mode='after')
    def need_emergency_contact(self):
        if self.age > 60 and 'emergency' not in self.contact:
            raise ValueError("Patients above 60 must provide a contact for emergency purposes")
        return self


patient_info = {"name": "Aman", "age": '67', "email": "amanbahare99@hdfc.com","linkedIn_URL": "https://chat.deepseek.com/", 
                "weight": 62, "allergies": ["polen", "dust"], "contact": {"email": "@ggndcom", "phone": "808500916", "emergency": "8934932489"} }

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