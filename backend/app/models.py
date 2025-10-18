from typing import Annotated, Optional
from sqlmodel import SQLModel, Field


class BlogPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    content: str