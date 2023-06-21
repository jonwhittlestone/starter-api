import uvicorn

from fastapi import Body, FastAPI, Depends, Request
from starlette.status import HTTP_201_CREATED
from .db import init_db, get_session
from .models import Album, AlbumCreate
from .config.dyna import settings

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI(title=settings.APP_NAME,)
app.mount("/static", StaticFiles(directory="backend/static"), name="static")
templates = Jinja2Templates(directory="backend/templates")

@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/health")
def health():
    return JSONResponse(status_code=200, 
                        content={
                            "app_name": settings.APP_NAME,
                            "current_env": settings.current_env,
                        })


@app.get("/")
def home(request: Request):
    # add a breakpoint on line below
    ...
    return {
        "heading": "Follow steps below to get vscode step debugging with FastAPI",
        "step-one": "Run `make up-build`",
        "step-two": "In vscode add a breakpoint",
        "step-three": "Run the debugger (F5)",
        "step-four": "Open the browser to http://127.0.0.1:8004",
        "step-five": "It will pause execution at the breakpoint"
    }
    #return templates.TemplateResponse("home.html", context={"request": request})

@app.get("/albums", response_model=list[Album])
async def get_songs(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Album))
    albums = result.scalars().all()
    return [
            Album(name=album.name, artist=album.artist, year=album.year, id=album.id) 
            for album in albums
    ]


@app.post("/albums", status_code=HTTP_201_CREATED, response_model=Album)
async def add_album(album: AlbumCreate, session: AsyncSession = Depends(get_session)):
    album = Album(name=album.name, artist=album.artist, year=album.year)
    session.add(album)
    await session.commit()
    await session.refresh(album)
    return album

