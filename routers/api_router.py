from fastapi import HTTPException, Query, APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from goods_model import Good


router = APIRouter()
templates = Jinja2Templates(directory="templates")


goods_list = [
    Good(
        title = "Гидрофильное гель-масло с витамином C «Кислородное дыхание» Oxiology",
        weight = 150,
        description = "Гидрофильное гель-масло с витамином C «Кислородное дыхание» разработано специально для мягкого очищения кожи без ощущения стянутости. Средство деликатно удаляет макияж и повседневные загрязнения, обеспечивая при этом абсолютный комфорт.",
        article = '3674',
        new_super = 'Новинка',
    ),
    Good(
        title="Дневной крем для лица «Кислородное питание» Oxiology",
        weight=51,
        description="Oxiology – уникальная система ежедневного ухода для каждого типа кожи. Средства серии решают самые разные задачи и способствуют улучшению кожного дыхания за счет качественного насыщения клеток кислородом.",
        article = '3691',
        new_super = 'Суперцена',
    ),
    Good(
        title="Отшелушивающий скраб для лица «Кислородное дыхание» Oxiology",
        weight=75,
        description="Отшелушивающий скраб для лица «Кислородное дыхание» глубоко и эффективно очищает кожу, делая ее ощутимо более мягкой и гладкой. Мягко удаляет ороговевшие клетки эпидермиса. Очищает поры, выравнивает микрорельеф кожи. Освежает, запускает процессы восстановления и улучшает усвоение кислорода кожей. Подготавливает кожу к следующим этапам ухода, увеличивая их эффективность",
        article = '3689',
        new_super = 'Суперцена',
    ),

    Good(
        title="Многофункциональный BB-крем для лица «Кислородное сияние» Oxiology",
        weight=32,
        description="Многофункциональный BB-крем для лица «Кислородное сияние» подстраивается под тон кожи и выравнивает его. Придает лицу мгновенный эффект естественного сияния. Содержит увлажняющие и обновляющие компоненты для дополнительного ухода за кожей. Шелковистая текстура крема легко распределяется по коже и не закупоривает поры. Подходит для всех типов кожи",
        article = '3696',
        new_super = 'Акция',
    ),
]


@router.get("/", response_class=HTMLResponse)
async def get_goods(request: Request):
    result = goods_list
    context = {
        "request": request,
        "title": "Каталог товаров",
        "goods": result
    }
    return templates.TemplateResponse("goods.html", context)

@router.get("/goods_search/", response_model=Good)
async def get_good_article(good_article: str):
    """Получить информацию по товару."""
    i = 0
    for g in goods_list:
        if g.article == good_article:
            i = 1
            return g
    if i == 0:
        raise HTTPException(status_code=404, detail="Good not found")




@router.post("/", response_model=Good, status_code=201)
async def create_good(good: Good):
    """Добавить новый товар."""
    for g in goods_list:
        if g.article == good.article:
            raise HTTPException(status_code=409, detail="Good already exists")

    goods_list.append(good)
    return good

