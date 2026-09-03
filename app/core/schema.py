from datetime import datetime
from pydantic import BaseModel

class NewUrl(BaseModel):
    url:str

class UrlResponse(NewUrl):
    slug:str
    criado_em:datetime
