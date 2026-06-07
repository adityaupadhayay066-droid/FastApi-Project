from fastapi import FastAPI,Request,Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database import cur,conn
from fastapi.responses import RedirectResponse
from datetime import date

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def redirect_home_page():
    return RedirectResponse("/home")

# Always return current date
today = date.today()

@app.get("/home", response_class=HTMLResponse)
def home_page(request:Request):
    cur.execute("SELECT *FROM  User_record")
    notes = cur.fetchall()
    return templates.TemplateResponse(
        request=request,name="index.html",
        context={"message":"Welcome to My Note App","notes":notes})

# getting name of user 
@app.get("/details/{note_id}", response_class=HTMLResponse)
def user_detail(request:Request, note_id:int):
   cur.execute("Select *from User_record where id=%s", (note_id,))
   note = cur.fetchone()
   if not note:
       return RedirectResponse("/home", status_code=303) 
   else:
        return templates.TemplateResponse(
        request=request,name="details.html",
        context={"message":"Your Note added Successfully!", "note":note}
    )
       
@app.post("/add", response_class=HTMLResponse)
def add_notes(request:Request,Work_type:str=Form(),Content:str=Form()):
    Work_type=Work_type.title()
    creation = str(date.today())
    print(Work_type)
    print(Content)
    print(creation)
    query = """
    Insert into User_record(Work_type, Content, creation_date)
    values(%s,%s,%s)
    """
    values = (Work_type,Content,creation)
    cur.execute(query, values)
    conn.commit()
    cur.execute("Select *from User_record") 
    notes = cur.fetchall()

    return templates.TemplateResponse(
        request=request,name="index.html",
        context={"message":"Note added Successfully!", "notes":notes})


@app.post("/delete/{note_id}")
def delete_user(note_id:int):
    query = "DELETE FROM User_record where id=%s"
    values = (note_id,)
    cur.execute(query, values)
    conn.commit()
    return RedirectResponse("/home", status_code=303)

