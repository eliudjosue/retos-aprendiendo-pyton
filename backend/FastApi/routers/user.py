from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user", tags=["user"], responses={404: {"error":"No encontrado"}})

# Iniciar el servidor: uvicorn users:app --reload

# Entidad User (Esto es como el tipado en typescript)
class User(BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int

users_list = [ User(id="1", name="eliud", surname="campos", url="http://eliudcampos.com.dev", age=34),
                  User (id="2", name="gaby", surname="garcia", url="http://gaby.com.dev", age=33),
                  User (id="3", name="Liam", surname="campos", url="http://liam.com.dev", age=3),
                  User (id="4", name="Sofi", surname="campos", url="http://sofi.com.dev", age=2)]

# Path
@router.get("/{id}")
async def user(id:int):
    return search_user(id)
    

# Query
@router.get("/")
async def user(id:int):
    return search_user(id)


@router.post("/", response_model=User, status_code = 201)
async def user(user: User):
    if isinstance(search_user(user.id), User):
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        users_list.append(user)
    return user

# put
@router.put("/")
async def user(user:User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return {"message": "Usuario actualizado exitosamente"}
    return {"error": "Usuario no encontrado"}


@router.delete("/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    if not found:
            return {"error":"No se ha eliminado el usuario"}

    
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
