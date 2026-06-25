from fastapi import FastAPI, Request, Form
from pydantic import BaseModel, Field,validator
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from logic import calculate_age

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

class DOB(BaseModel):
    day:int = Field(ge=1,le=31)
    month:int = Field(ge=1,le=12)
    year:int = Field(ge=1900,le=2026)


@app.get("/home", response_class=HTMLResponse)
def Home_page(request:Request):
    return templates.TemplatesResponse(request=request,name="index.html")

@app.post("/calculate", response_class=HTMLResponse)
def calculate_DOB(request:Request,dob:str=Form()):
    date_obj = date.strptime(dob, "%d/%m/%Y")
    date = date_obj.date
    month = date_obj.month
    year = date_obj.year
    return templates.TemplateResponse("name"="index.html"
                                      {"request":request,"age":age})


 