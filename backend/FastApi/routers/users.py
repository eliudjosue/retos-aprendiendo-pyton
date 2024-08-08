from fastapi import APIRouter
from pydantic import BaseModel

class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int

router = APIRouter(prefix="/users", tags=["users"], responses={404: {"error":"No encontrado"}})

users_list = [ User(id="1", name="eliud", surname="campos", url="http://eliudcampos.com.dev", age=34),
                  User (id="2", name="gaby", surname="garcia", url="http://gaby.com.dev", age=33),
                  User (id="3", name="Liam", surname="campos", url="http://liam.com.dev", age=3),
                  User (id="4", name="Sofi", surname="campos", url="http://sofi.com.dev", age=2)]

@router.get("/")
async def userclass():
    return users_list
