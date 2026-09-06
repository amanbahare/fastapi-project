from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def hello():
    return {"Hello" : "i am FastAPI"} 

@app.get("/about")
def about(name: str = "Aman", goal: str = "Master in AI/ LLM Engineering/ Agentic AI systems"):
    return {"name": name,
             "goal": goal}
