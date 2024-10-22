from fastapi import FastAPI
from data import projectsOut

app = FastAPI()

@app.get("/")
def index():
    return {"name":"Welcome to Arctech"}

@app.get("/projects")
def get_projects():
    return projectsOut 