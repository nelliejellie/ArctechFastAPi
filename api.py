from fastapi import FastAPI,Path
from data import projectsOut
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

class Project(BaseModel):
    id:int
    title:str
    description:str
    image_url:str
    project_url: str

class UpdateProject(BaseModel):
    id : int = None
    title:str = None
    description:str = None
    image_url:str = None
    project_url: str = None

@app.get("/")
def index():
    return {"name":"Welcome to Artech"}

@app.get("/projects")
def get_projects():
    return projectsOut 

#path parameter
@app.get("/get-project/{project_id}")
def get_project(project_id:int):
    for project in projectsOut:
        if project["id"] == project_id:
            print(project)
            return project
    return {"message":"data does not exist"}


#query parameter
@app.get("/get-by-title")
def get_student(name:str):
    for project in projectsOut:
        if project["title"] == name:
            return project
    return {"message":"data does not exist"}

# post method
@app.post("/create-project/{project_id}")
def create_project(project_id: int, project: Project):
    if project_id in projectsOut:
        return {"ErrorMsg": "Project exists"}
    projectsOut[project_id] = project
    return projectsOut[project_id]

@app.put("/create-project/{project_id}")
def update_project(project_id: int, project: Project):
    if project_id not in projectsOut:
        return {"ErrorMsg": "Student exists"}
    if project.title != None:
        projectsOut[project_id].title = project.title
    if project.description != None:
        projectsOut[project_id].description = project.title
    if project.image_url != None:
        projectsOut[project_id].image_url = project.title
    if project.project_url != None:
        projectsOut[project_id].project_url = project.title
    projectsOut[project_id] = project
    return projectsOut[project_id]

@app.delete("/delete-project/[roject_id]")
def delete_project(project_id: int):
     if project_id not in projectsOut:
        return {"ErrorMsg": "project does not exists"}
     
     del projectsOut[project_id]
     return {"Message": "Project deleted successfully"}