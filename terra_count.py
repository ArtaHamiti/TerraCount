from enum import Enum, auto

import pandas as pd
from pathlib import Path

categories_str_list = ["Terraforming points", "Milestones", "Awards", "Forests", "City points", "Project points"]


def count_terra_points(players: list, date_str: str, file_path: Path):
    headers = [player for player in players]
    all_lists = [count_category(players, category) for category in categories_str_list]
    df = pd.DataFrame(data=all_lists, columns=headers, index=categories_str_list).transpose()
    df["Total score"] = df.sum(axis="columns")
    winner = df["Total score"].idxmax()
    print_congratulations(winner)
    with open(file_path, "a") as f:
        f.write(date_str)
        f.write(df.to_csv())


def print_congratulations(winner: str):
    print("-------------------------------------------------")
    print(f"|  {winner} is the best, wooooo :D Congratulations! |")
    print("-------------------------------------------------")


def count_category(players: list, category: str) -> list:
    points_list = []
    for player in players:
        number = int(input(f"Number of {category} for {player}:"))
        if category == "Milestones":
            number = number * 5
        elif category == "Awards":
            number = number * 5  # todo: if players are 2 or more, 1st and 2nd place
        points_list.append(number)
    return points_list


def main():
    file_path = Path(__file__).parent / "TerraCount_score_sheet_test.csv"
    no_of_players = int(input("How many players?: "))
    names = [input(f"Please write in player {i + 1}: ") for i in range(no_of_players)]
    date_str = input("Please write today's date in the format 'dd.mm.yy': ")
    count_terra_points(names, date_str, file_path)


if __name__ == "__main__":
    main()
