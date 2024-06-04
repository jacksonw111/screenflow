from sqlmodel import SQLModel


class PageModel(SQLModel):
    name: str
