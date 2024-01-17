from fastapi import FastAPI, Depends, Request, Form, status

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from fastapi.responses import JSONResponse


from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import json
models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI(swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
# app = FastAPI()
# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

@app.get("/")
async def home(req: Request, db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    todos_dict = [todo.__dict__ for todo in todos]
    return todos_dict#JSONResponse(content=todos_dict)
    # return templates.TemplateResponse("base.html", { "request": req, "todo_list": todos })

@app.post("/add")
def add(req: Request, title: str = Form(...), db: Session = Depends(get_db)):
    new_todo = models.Todo(title=title)
    db.add(new_todo)
    db.commit()
    # url = app.url_path_for("home")
    # return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
    todos = db.query(models.Todo).all()
    todos_dict = [todo.__dict__ for todo in todos]
    return todos_dict

@app.get("/update/{todo_id}")
def add(req: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()
    # url = app.url_path_for("home")
    # return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
    todos = db.query(models.Todo).all()
    todos_dict = [todo.__dict__ for todo in todos]
    return todos_dict


@app.get("/delete/{todo_id}")
def add(req: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    # url = app.url_path_for("home")
    # return RedirectResponse(url=url, status_code=status.HTTP_303_SEE_OTHER)
    todos = db.query(models.Todo).all()
    todos_dict = [todo.__dict__ for todo in todos]
    return todos_dict

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)