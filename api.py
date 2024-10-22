from fastapi import FastAPI
from data import projectsOut
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)
@app.get("/")
def index():
    return {"name":"Welcome to Artech"}

@app.get("/projects")
def get_projects():
    return projectsOut 

@app.get("/get-project/{project_id}")
def get_project(project_id:int):
    for project in projectsOut:
        if project["id"] == project_id:
            print(project)
            return project
    return {"message":"data does not exist"}