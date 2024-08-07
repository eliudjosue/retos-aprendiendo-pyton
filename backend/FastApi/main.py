from fastapi import FastAPI

app = FastAPI()

#URL LOCAL: http://127.0.0.1:8000/

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