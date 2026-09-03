from .core.server import app

from app.views import api

app.include_router(api)
