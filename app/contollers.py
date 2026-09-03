from .utils import gerar_codigo
from .core.schema import NewUrl, UrlResponse
from .models import (
    Url,
    UrlAnalytic,
)
from fastapi import Request, HTTPException
from fastapi.responses import RedirectResponse

def redirecionar_usuario(request:Request, id:str):

    url = Url.get_or_none(Url.slug == id)
    if url:
        UrlAnalytic.create(url=url)
        
        return RedirectResponse(url.url, status_code=302)
    
    raise HTTPException(404, "Url não encontrada")

async def encurtar_url(request:Request, data:NewUrl):

    code = gerar_codigo(tamanho=8)
    url = Url.create(
        url=data.url,
        slug=code,
    )
    redirect_url = f"{request.url}/{code}".replace("//", "/")

    return UrlResponse(
        url=redirect_url,
        slug=code,
        criado_em=url.criado_em
    )


def analise_acessos(url:str):

    return ...

