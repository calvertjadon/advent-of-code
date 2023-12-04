import math
import sys

def calculate_result(scratch_card: str) -> int:
    _, rest = scratch_card.strip().split(": ")
    winning_numbers, card_numbers = rest.strip().split(" | ")
    
    winning_numbers = winning_numbers.split(" ")
    card_numbers = card_numbers.split(" ")

    matches = [n for n in card_numbers if n in winning_numbers]
    return int(math.pow(2, len(matches) - 1))


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        total += calculate_result(line)

    print(total)

