import argparse

from pathlib import Path


DIGITS = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
]


def calculate_line_cv(line: str) -> int:
    digits = []
    for i in range(len(line)):
        if line[i].isdigit():
            digits.append(line[i])
            continue

        for word, n in DIGITS:
            if line[i:].startswith(word):
                digits.append(str(n))
                i += len(word)

    # print(f"line={line}, digits={digits}")
    first, last = digits[0], digits[-1]
    return int(first + last)


def calculate_document_cv(calibration_document: Path) -> int:
    total = 0
    with open(calibration_document, "r") as f:
        for line in f.readlines():
            if not line.strip():
                continue

            cv = calculate_line_cv(line)
            total += cv

    return total


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("calibration_document", type=Path)
    return parser.parse_args()


def main():
    cv = calculate_document_cv(parse_args().calibration_document)
    print(cv)


if __name__ == "__main__":
    main()
