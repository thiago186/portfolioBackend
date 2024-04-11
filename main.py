from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from Connection.mongodb_connector import db_manager
from schemas.config import settings
from schemas.project_schema import ProjectSchema, ProjectSchemaOptional
from schemas.exceptions import ObjectIdException

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/projects")
def read_projects():
    all_items = db_manager.get_all_items()
    return all_items

@app.get("/projects/{project_id}")
def get_project(project_id: str):
    try:
        project = db_manager.get_item({"_id": project_id})
        return project
    except Exception as e:
        return {}
    
@app.post("/projects")
def create_project(project: ProjectSchema):
    try:
        item_id = db_manager.insert_item(project.model_dump())
        return {"id": str(item_id)}
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.put("/projects/{project_id}")
def update_project(project_id: str, project: ProjectSchemaOptional):
    try:
        result = db_manager.update_item({"_id": project_id}, project.model_dump(exclude_none=True))
        return {"modified_count": str(result)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/projects/{project_id}")
def delete_project(project_id: str, password: str):
    if password != settings.delete_password:
        raise HTTPException(status_code=400, detail="Invalid password")
    
    try:
        result = db_manager.delete_item({"_id": project_id})
        return {"deleted_count": str(result)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))