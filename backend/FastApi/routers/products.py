from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"error":"No encontrado"}})

product_list = ["producto 1","producto 2","producto 3","producto 4","producto 5"]

@router.get("/")
async def userclass():
    return product_list

@router.get("/{id}")
async def userclass(id:int):
    return product_list[id]