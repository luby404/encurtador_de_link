from fastapi import APIRouter, Request


from .contollers import (
    encurtar_url,
    redirecionar_usuario,
    analise_acessos
)

from .core.schema import NewUrl

api = APIRouter(
    tags=["links"],
)

@api.get("/{id}")
async def get_redirect_url(request:Request, id:str):
    return redirecionar_usuario(request, id)

@api.post("/")
async def create_new_link(request:Request, url:NewUrl):
    return encurtar_url(request, url)


@api.get("/analitc/<id>")
async def analitic(id):
    return analise_acessos(id)

