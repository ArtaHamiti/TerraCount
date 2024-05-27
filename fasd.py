from typing import Union
from csv import DictReader
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
import logging

environment = Environment(loader=FileSystemLoader("templates/"))
app = FastAPI()


@app.get("/")
def read_root():
    template = environment.get_template("frontpage.html.j2")
    with open("Terraforming_score_sheet.csv") as f:
        games = DictReader(f, delimiter=',', quotechar='"')
        users = [game["Name"] for game in games]
    return HTMLResponse(template.render({"users": users}))


@app.get("/games2")
def read_root():
    template = environment.get_template("all_games.html.j2")
    with open("Terraforming_score_sheet.csv") as f:
        games = DictReader(f, delimiter=',', quotechar='"')
        headers = games.fieldnames
        games = list(games)
    print("games:", str(games))
    return HTMLResponse(template.render({"games": list(games), "headers": headers}))


@app.get("/new_game")
def read_root():
    template = environment.get_template("new_game.html.j2")
    return HTMLResponse(template.render())


@app.get("/games/{game_id}")
def read_item(game_id: str, q: Union[str, None] = None):
    return {"game_id": game_id, "q": q}


@app.post("/all_games/")
def read_item(game: str = Form()):
    return game
