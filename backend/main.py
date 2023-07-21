from fastapi import Body, FastAPI, Depends, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .db import init_db
from .config import setts
from .api.endpoints import routers


app = FastAPI(
    title=setts.SERVICE_LABEL,
    description=setts.SERVICE_DESCRIPTION,
    version=setts.SERVICE_VERSION,
    debug=setts.DEBUG,
)

app.mount("/static", StaticFiles(directory="backend/static"), name="static")
templates = Jinja2Templates(directory="backend/templates")


@app.on_event("startup")
async def on_startup():
    await init_db()


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
        "step-five": "It will pause execution at the breakpoint",
    }


# register routes
app.include_router(routers, prefix="/api/v1")
