from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
# import databases
# import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from models import Base, Client
from models import Base
import crud, schemas
from sqlalchemy.orm import Session

app = FastAPI()
templates = Jinja2Templates(directory="templates")
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@127.0.0.1:6432/flask"
e = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=e)

Base.metadata.create_all(e)

# @app.on_event("startup")
# async def startup():
#     # print(engine)
#     print(Base)
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/client/", response_model=schemas.Client)
def create_client(first_name: str, second_name: str, client: schemas.ClientCreate, db: Session = Depends(get_db)):
    print("new client")
    return crud.create_client(db=db, client=client, first_name=first_name, second_name=second_name)

# @app.post("/items/{user_id}/", response_model=schemas.Item)
# def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
#     print("new new")
#     # c = crud.create_user_item(db=db, user_id=user_id)
#     return crud.create_user_item(db=db, item=item, user_id=user_id)

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    print("new 1")
    return templates.TemplateResponse("index.html", {"request": request})

# @app.post("/items/")
# async def create_item(entItem: Item):
#     print('hello world')
#     return {"item": entItem}
