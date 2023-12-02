import argparse
import math

from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=Path)
    return parser.parse_args()


def check_game_is_possible(round_details: str, available: dict[str, int]) -> bool:
    for round in round_details.split(";"):
        dice_sets = round.strip().split(", ")

        for dice_set in dice_sets:
            quantity, color = dice_set.split(" ")
            quantity = int(quantity)

            if available[color] < quantity:
                return False

    return True


def sum_possible_game_ids(game_records: list[str], bag: dict[str, int]):
    games = {True: [], False: []}

    for line in game_records:
        game_details, round_details = line.split(":")

        _, game_id = game_details.split(" ")
        game_id = int(game_id)

        result = check_game_is_possible(round_details, available={**bag})
        games[result].append(game_id)

    return sum(games[True])


def calculate_min_requirements(round_details: str) -> dict[str, int]:
    dice = {}

    for round in round_details.split(";"):
        dice_sets = round.strip().split(", ")

        for dice_set in dice_sets:
            quantity, color = dice_set.split(" ")
            quantity = int(quantity)

            dice.setdefault(color, 0)
            dice[color] = max(dice[color], quantity)

    return dice


def sum_powers(game_records: list[str]):
    powers = []

    for line in game_records:
        _, round_details = line.split(":")

        set_power = math.prod(calculate_min_requirements(round_details).values())
        powers.append(set_power)

    return sum(powers)


if __name__ == "__main__":
    args = parse_args()
    input_file: Path = args.input_file

    bag = {"red": 12, "green": 13, "blue": 14}
    game_records = input_file.read_text().strip().splitlines()

    result = sum_possible_game_ids(game_records, bag)
    print(result)

    result = sum_powers(game_records)
    print(result)

