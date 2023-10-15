from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from item import Item
import databases
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey
# from models import Base, Client
from models import Base

app = FastAPI()
templates = Jinja2Templates(directory="templates")
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@127.0.0.1:6432/flask"
e = create_engine(DATABASE_URL)

Base.metadata.create_all(e)
# database = databases.Database(DATABASE_URL)
# metadata = sqlalchemy.MetaData()

# engine = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(engine)

# @app.on_event("startup")
# async def startup():
#     # print(engine)
#     print(Base)
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/items/")
async def create_item(entItem: Item):
    print('hello world')
    return {"item": entItem}
