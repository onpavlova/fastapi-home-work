from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from urllib3 import request

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {
        "request": request,
        "title": "Магазин косметики",
        "user": "Ольга"
    }
    return templates.TemplateResponse("index.html",context)


@router.get("/about/")
async def about(request: Request):
    context = {
        "request": request,
        "title": "Магазин косметики",
        "content": "Сайт содержит информацию о товарах косметического магазина. Автор: Павлова ОН"
    }
    return templates.TemplateResponse("about.html", context)

