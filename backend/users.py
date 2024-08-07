from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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

@app.get("/usersJson")
async def usersjson():
    return[{"name":"eliud", "surname":"campos", "url":"http://:eliudcampos.com.dev", "age":34},{"name":"gabriela", "surname":"garcia", "url":"http://:gaby.com.dev", "age":33},{"name":"liam", "surname":"campos", "url":"http://:liam.com.dev", "age":3},{"name":"sofi", "surname":"campos", "url":"http://:sofi.com.dev", "age":2},]

@app.get("/users")
async def userclass():
    return users_list

# Path
@app.get("/user/{id}")
async def user(id:int):
    return search_user(id)
    

# Query
@app.get("/user/")
async def user(id:int):
    return search_user(id)


@app.post("/user/")
async def user(user: User):
    if isinstance(search_user(user.id), User):
        return {"error":"El usuario ya existe"}
    else:
        users_list.append(user)
    return user


@app.put("/user/")
async def user(user:User):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            return {"message": "Usuario actualizado exitosamente"}
    return {"error": "Usuario no encontrado"}


@app.delete("/user/{id}")
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
