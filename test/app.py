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




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)