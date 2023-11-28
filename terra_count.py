from enum import Enum, auto
from datetime import date, datetime

import pandas as pd
from pathlib import Path

# todo: better way to do this?
terra_points = "Terraforming points"
milestones = "Milestones"
awards = "Awards"
second_places = "Second place awards"
forests = "Forests"
city_points = "City points"
project_points = "Project points"
categories_str_list = [terra_points, milestones, awards, second_places, forests, city_points, project_points]


def count_terra_points(players: list) -> pd.DataFrame:
    if len(players) < 3:
        categories_str_list.remove(second_places)
    category_lists = [count_category(players, category) for category in categories_str_list]
    df = pd.DataFrame(data=category_lists, columns=players, index=categories_str_list).transpose()
    df["Total score"] = df.sum(axis="columns")
    if len(players) > 2:
        df[awards] = df[awards] + df[second_places]
        df.drop(columns=[second_places], axis=1, inplace=True)
    return df


def print_congratulations(winner: str):
    print("-------------------------------------------------")
    print(f"|  {winner} is the best, wooooo :D Congratulations! |")
    print("-------------------------------------------------")


def count_category(players: list, category: str) -> list:
    points_list = []
    category_count = 0
    for i, player in enumerate(players):
        if category_count >= 3:
            print(f"All {category.lower()} have been taken. Moving on to next category.")
            players_left = len(players) - i
            for j in range(players_left):
                points_list.append(0)
            return points_list

        number = input(f"Number of {category.lower()} for {player}: ")
        number = input_to_int(number, category)

        if category == milestones or category == awards:
            category_count += number
            number = number * 5
        elif category == second_places:
            category_count += number
            number = number * 2

        points_list.append(number)
    return points_list


def input_to_int(input_str: str, type_of_input: str) -> int:
    lower = -4
    upper = 181
    if type_of_input == "players":
        lower = 1
        upper = 5
    elif type_of_input in {awards, milestones, second_places}:
        lower = 0
        upper = 3
    input_str = input_str.strip()
    while not (input_str.isdigit()) or (input_str is None) or int(input_str) < lower or int(input_str) > upper:
        input_str = input(f"{input_str} is not valid, please put in a positive integer between {lower} and {upper}: ")
    return int(input_str)


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


def input_not_none_or_digit(name: str) -> str:
    while (len(name) < 3) or (name.isdigit()) or (len(name) > 11):
        name = input("Not valid, please write the name again: ")
    return name


def main():
    file_path = Path(__file__).parent / "TerraCount_score_sheet_test.csv"
    no_of_players = input_to_int(input("How many players are you?: "), "players")
    names = [input_not_none_or_digit(input(f"Please write the name of player {i + 1}: ")) for i in range(no_of_players)]
    date_object = input_to_date("Please write today's date in the format 'dd.mm.yy': ")
    df = count_terra_points(names)
    winner = df["Total score"].idxmax()
    print_congratulations(winner)
    with open(file_path, "a") as f:
        f.write(str(date_object))
        f.write(df.to_csv())


if __name__ == "__main__":
    main()