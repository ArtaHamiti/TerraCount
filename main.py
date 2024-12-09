from typing import Union
from csv import DictReader
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
import logging

from starlette.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    with open("Terraforming_score_sheet.csv") as f:
        games = DictReader(f, delimiter=',', quotechar='"')
        users = [game["Name"] for game in games]
    return templates.TemplateResponse(request, name="frontpage.html.j2", context={"users": users})


@app.get("/games2")
def read_root(request: Request):
    with open("Terraforming_score_sheet.csv") as f:
        games = DictReader(f, delimiter=',', quotechar='"')
        headers = games.fieldnames
        games = list(games)
    print("games:", str(games))
    return templates.TemplateResponse(request, name="all_games.html.j2", context={"games": list(games), "headers": headers})


@app.get("/test/")
def read_root(request: Request):
    return templates.TemplateResponse(request, name="test.html.j2")


@app.get("/new_game")
def read_root(request: Request):
    return templates.TemplateResponse(request, name="new_game.html.j2")


@app.get("/games/{game_id}")
def read_item(game_id: str, q: Union[str, None] = None):
    return {"game_id": game_id, "q": q}


@app.post("/all_games/")
def read_item(game: str = Form()):
    return game