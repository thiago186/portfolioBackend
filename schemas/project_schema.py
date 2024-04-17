from pydantic import BaseModel
from typing import Optional


class ProjectSchema(BaseModel):
    is_active: bool = True
    image_url: str
    project_name: str
    project_description: str
    project_markdown_page: str
    github_url: str


class ProjectSchemaOptional(BaseModel):
    is_active: Optional[bool] = True
    image_url: Optional[str] = None
    project_name: Optional[str] = None
    project_description: Optional[str] = None
    project_markdown_page: Optional[str] = None
    github_url: Optional[str] = None


if __name__ == "__main__":
    project = ProjectSchema(
        image_url="https://th.bing.com/th?id=OSK.fb73dd685cdffd3522bdf9258e1976dc",
        project_name="Projeto 1",
        project_description="Descrição do projeto",
        github_url="https://github.com"
    )
    print(project)
    print(project.model_dump())
    
    optional_project = ProjectSchemaOptional(image_url="https://www.google.com", project_name="Projeto 1")
    optional_project.model_dump(exclude_none=True)