import pytest

from pathlib import Path

from aoc2023.day1 import calculate_document_cv, calculate_line_cv


@pytest.mark.parametrize(
    "sample_input,expected",
    [("1abc2", 12), ("pqr3stu8vwx", 38), ("a1b2c3d4e5f", 15), ("treb7uchet", 77)],
)
def test_part_one_sample_input(sample_input: str, expected: int):
    result = calculate_line_cv(sample_input)
    assert result == expected


def test_part_one_sum(tmp_path: Path):
    input_file = tmp_path / "cv_doc.txt"
    input_file.write_text(
        """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
    )
    cv = calculate_document_cv(input_file)
    assert cv == 142


@pytest.mark.parametrize(
    "sample_input,expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_part_two_sample_input(sample_input: str, expected: int):
    result = calculate_line_cv(sample_input)
    assert result == expected
