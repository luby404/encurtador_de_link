from fastapi import APIRouter
from fastapi.responses import RedirectResponse

api = APIRouter(
    tags=["encurtador de link"],
)

@api.get("/{id}")
def get_redirect_url(id:str):
    url = "https://www.google.com"

    return RedirectResponse(url, status_code=302)

@api.post("/")
def create_new_link():

    return {}



@api.get("/analitc/<id>")
def analitic(id):

    return {}