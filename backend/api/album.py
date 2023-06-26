from fastapi import APIRouter, Depends, status


from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models import Album, AlbumCreate
from ..db import init_db, get_session

routers = APIRouter()

@routers.get("/albums", response_model=list[Album])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Album))
    albums = result.scalars().all()
    return [
            Album(name=album.name, artist=album.artist, year=album.year, id=album.id) 
            for album in albums
    ]


@routers.post("/albums", status_code=status.HTTP_201_CREATED, response_model=Album)
async def add_album(album: AlbumCreate, session: AsyncSession = Depends(get_session)):
    album = Album(name=album.name, artist=album.artist, year=album.year)
    session.add(album)
    await session.commit()
    await session.refresh(album)
    return album