from pydantic import BaseModel

class Address(BaseModel):

    city : str 
    state : str 
    pincode : int 

class Patient(BaseModel):

    name : str 
    age : int 
    weight : int 
    address : Address   


address_info = {"city": "pune", "state": "maharashtra", "pincode": 462033}
address1 = Address(**address_info)

patient_info = {"name": "aman", "age": 27, "weight": 62, "address" : address1}
p1 = Patient(**patient_info)

print("entire_patient_information : ",p1)
print("only pincode :",p1.address.pincode)
print("only address :",p1.address)