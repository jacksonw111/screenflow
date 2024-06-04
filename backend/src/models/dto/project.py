from typing import Optional
from sqlmodel import SQLModel


class ProjectModel(SQLModel):
    name: str
    current_version_name: str
    current_version_description: str
    description: Optional[str] = None
