from pydantic import BaseModel

class Address(BaseModel):
    city : str 
    state : str 
    pincode : int 

class Patient(BaseModel):
    name : str 
    age : int 
    gener : str = "male"
    weight : int 
    address : Address   

address_info = {"city": "pune", "state": "maharashtra", "pincode": 462033}
address1 = Address(**address_info)

patient_info = {"name": "aman", "age": 27, "weight": 62, "address" : address1}
p1 = Patient(**patient_info)

print("entire_patient_information : ",p1)

temp = p1.model_dump() 
temp1 = p1.model_dump_json() # for exporting in JSON type
print("dumping to dict :", temp)
print("dumping to json :", temp1)  
print("type of temp :", type(temp))

print(p1.model_dump(include='name''address'))
print(p1.model_dump(exclude='weight'))
print(p1.model_dump(exclude={'age': True, 'address': {'state': True}}))

temp2 = p1.model_dump(exclude_unset=True)
print("temp2 :",temp2)