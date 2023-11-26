from enum import Enum, auto
from datetime import date, datetime

import pandas as pd
from pathlib import Path

categories_str_list = ["Terraforming points", "Milestones", "Awards", "Forests", "City points",
                       "Project points"]


def count_terra_points(players: list, date_object: date, file_path: Path, no_of_players: int):
    headers = [player for player in players]
    all_lists = [count_category(players, category, no_of_players) for category in categories_str_list]
    df = pd.DataFrame(data=all_lists, columns=headers, index=categories_str_list).transpose()
    df["Total score"] = df.sum(axis="columns")
    winner = df["Total score"].idxmax()
    print_congratulations(winner)
    with open(file_path, "a") as f:
        f.write(str(date_object))
        f.write(df.to_csv())


def print_congratulations(winner: str):
    print("-------------------------------------------------")
    print(f"|  {winner} is the best, wooooo :D Congratulations! |")
    print("-------------------------------------------------")


def count_category(players: list, category: str, no_of_players: int) -> list:
    points_list = []
    for player in players:
        try:
            number = int(input(f"Number of {category} for {player}: "))
        except ValueError:
            print("Not an integer")
        if category == "Milestones":
            number = number * 5
        elif category == "Awards":
            if no_of_players > 2:
                second_places = int(input(f"How many 2nd place awards did {player} get?: "))
            else:
                second_places = 0
            number = number * 5 + second_places * 2
        points_list.append(number)
    return points_list


def input_to_int(question: str) -> int:
    input_value = input(question).strip()
    while not input_value.isdigit():
        input_value = input(f"{input_value} is not valid, please put in a positive integer: ")
    return int(input_value)


def is_date_input_valid(input_value: str, format_str: str) -> bool:
    try:
        bool(datetime.strptime(input_value, format_str))
        return True
    except ValueError:
        return False


def input_to_date(question: str) -> date:
    format_str = "%d.%m.%Y"
    user_input = input(question)
    input_value = is_date_input_valid(user_input, format_str)
    while not input_value:
        correction_str = f"{user_input} is not in the correct format, please use the format 'dd.mm.yyyy': "
        user_input = input(correction_str)
        input_value = is_date_input_valid(user_input, format_str)
    return datetime.strptime(user_input, format_str).date()


def main():
    file_path = Path(__file__).parent / "TerraCount_score_sheet_test.csv"
    no_of_players = input_to_int("How many players are you?: ")
    names = [input(f"Please write the name of player {i + 1}: ") for i in range(no_of_players)]
    date_object = input_to_date("Please write today's date in the format 'dd.mm.yy': ")
    count_terra_points(names, date_object, file_path, no_of_players)


if __name__ == "__main__":
    main()
