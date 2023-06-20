from typing import Optional
from sqlmodel import SQLModel, Field

class AlbumBase(SQLModel):
    name: str
    artist: str
    year: Optional[int] = None

class Album(AlbumBase, table=True):
    
    id: int = Field(default=None, primary_key=True)

class AlbumCreate(AlbumBase):
    extend_existing=True
    pass