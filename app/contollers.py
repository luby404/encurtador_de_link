from .utils import gerar_codigo
from .core.schema import NewUrl, UrlResponse
from .models import (
    Url,
    UrlAnalytic,
)
from fastapi import Request

def redirecionar_usuario():

    return ...

def encurtar_url(request:Request, data:NewUrl):

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

