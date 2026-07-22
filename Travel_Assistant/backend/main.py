from fastapi import FastAPI
# from database import engine
# from Datasets import train
from fastapi import Request,Form 
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse,RedirectResponse

app = FastAPI(title="Ai Tarvel Assistant")

templates = Jinja2Templates(directory="frontend")

@app.get("/")
def redirect():
    return RedirectResponse("/home")

@app.get("/home")
def greet():
    return{"Welcome to Ai Travell Assistant"}
