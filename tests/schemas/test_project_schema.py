import pytest
from pydantic import ValidationError
from ...schemas.project_schema import ProjectSchema

def test_project_schema_valid_data():
    """Valid data"""
    data = {
        "image_url": "https://example.com/image.jpg",
        "project_name": "My Project",
        "project_description": "This is my project"
    }
    project = ProjectSchema(**data)
    assert project.image_url == data["image_url"]
    assert project.project_name == data["project_name"]
    assert project.project_description == data["project_description"]


def test_project_schema_invalid_data():
    """Invalid data"""
    invalid_data = {
        "image_url": "https://example.com/image.jpg",
        "project_name": "My Project",
        "project_description": 123  # Invalid type
    }
    with pytest.raises(ValidationError):
        ProjectSchema(**invalid_data)