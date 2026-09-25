from fastapi import FastAPI, Path, Query, HTTPException
import json 

app = FastAPI()

@app.get("/")
def hello():
    return {"Hello" : "i am FastAPI"} 

@app.get("/about")
def about(name: str = "Aman", goal: str = "Master in AI/ LLM Engineering/ Agentic AI systems"):
    return {"name": name,
             "goal": goal}

def load_data():
    with open('patients.json', 'r') as file:
        return json.load(file)

@app.get("/view")  
def view():
    data = load_data()
    return data 

@app.get("/patient/{patient_id}")
def patientid(patient_id : str = Path(..., description="Please provide the Patient ID", examples="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient ID is wrong")

@app.get("/sort")
def sort_patient(sort_by : str = Query(..., description= "sort by hieght, weight or bmi"),
                 order : str = Query('asc', description= "sort in asc or desc")):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail= f"please provide from {valid_fields}")

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=404, detail="it can be asc or desc")

    data = load_data()

    order_by = True if order == 'asc' else False
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse= order_by)
    return sorted_data
 