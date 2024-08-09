from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import user, users, basic_auth_users
from routers import products

app = FastAPI()

# Clase en vídeo: https://youtu.be/_y9qQZXE24A?t=12475
app.include_router(products.router)
app.include_router(user.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(basic_auth_users.router)


@app.get("/")
async def root():
    return "!Hola FastApi!"

# Url local: http://127.0.0.1:8000/url

@app.get("/url")
async def url():
    return { "http://eliudjosue.dev/python"}

# Iniciar el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentacion swagger: http://127.0.0.1:8000/docs

# Documentacion Redocly: http://127.0.0.1:8000/redoc