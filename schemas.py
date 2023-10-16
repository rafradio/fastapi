from pydantic import BaseModel, Field

class ClientBase(BaseModel):
    email: str
    password: str 

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    id: int
    first_name: str
    second_name: str

    class Config:
        orm_mode = True