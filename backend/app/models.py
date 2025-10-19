from typing import Annotated, Optional, List
from sqlmodel import SQLModel, Field, Column, DateTime
from datetime import datetime
import sqlalchemy as sa
from .config import indian_timezone


class BlogPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    content: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(indian_timezone),
                                 sa_column=Column(DateTime(timezone=True), nullable=False))
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(indian_timezone),
        sa_column=Column(DateTime(timezone=True), nullable=False, onupdate=lambda: datetime.now(indian_timezone))
    )
    tags: Optional[str] = Field(default='', description="Comma-separated tags for the blog post")
    location: Optional[str] = Field(sa_column=sa.String(100), default=None)


    @property
    def tags_list(self) -> List[str]:
        return [tag.strip() for tag in self.tags.split(",") if tag.strip()]

    @tags_list.setter
    def tags_list(self, value: List[str]):
        self.tags = ",".join(value)