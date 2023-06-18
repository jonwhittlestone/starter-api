from fastapi import Body, FastAPI, Form, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="backend/static"), name="static")
templates = Jinja2Templates(directory="backend/templates")



@app.get("/")
def home(request: Request):
    # add a breakpoint on line below
    ...
    return {
        "heading": "Follow steps below to get vscode step debugging with FastAPI",
        "step-one": "Run `make up-dbg-build`",
        "step-two": "In vscode add a breakpoint",
        "step-three": "Run the debugger (F5)",
        "step-four": "Open the browser to http://localhost:8004",
        "step-five": "It will pause execution at the breakpoint"
    }
    #return templates.TemplateResponse("home.html", context={"request": request})


@app.post("/tasks", status_code=201)
def run_task(payload = Body(...)):
    task_type = payload["type"]
    return JSONResponse(task_type)


@app.get("/tasks/{task_id}")
def get_status(task_id):
    return JSONResponse(task_id)