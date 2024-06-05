from sqlmodel import SQLModel


class ScenarioModel(SQLModel):
    name: str
