import pytest


from aoc2023.day2 import check_game_is_possible, sum_possible_game_ids


@pytest.mark.parametrize(
    "sample_record,expected",
    [
        ("3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green", True),
        ("1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue", True),
        (
            "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            False,
        ),
        (
            "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            False,
        ),
        ("6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green", True),
    ],
)
def test_part_one_sample_input(sample_record: str, expected: bool):
    bag = {"red": 12, "green": 13, "blue": 14}
    
    result = check_game_is_possible(sample_record, available={**bag})
    assert result == expected


def test_calculate_sum():
    samples_records = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""
    bag = {"red": 12, "green": 13, "blue": 14}
    result = sum_possible_game_ids(samples_records.strip().splitlines(), bag)
    assert result == 8
