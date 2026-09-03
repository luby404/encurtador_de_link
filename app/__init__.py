from .core.server import app

from app.views import api
from app.models import init_models

init_models()
app.include_router(api)

