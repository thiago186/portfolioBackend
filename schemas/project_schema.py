from pydantic import BaseModel
from typing import Optional


class ProjectSchema(BaseModel):
    image_url: str
    project_name: str
    project_description: str

class ProjectSchemaOptional(BaseModel):
    image_url: Optional[str] = None
    project_name: Optional[str] = None
    project_description: Optional[str] = None    


if __name__ == "__main__":
    project = ProjectSchema(image_url="https://www.google.com", project_name="Projeto 1", project_description="Descrição do projeto")
    print(project)
    print(project.model_dump())
    
    optional_project = ProjectSchemaOptional(image_url="https://www.google.com", project_name="Projeto 1")
    optional_project.model_dump(exclude_none=True)