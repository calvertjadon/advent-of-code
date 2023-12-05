from collections import defaultdict
import math
import sys


class Scratchcard:
    id: int
    winning_numbers: list[int]
    card_numbers: list[int]

    def __init__(
        self, id: int, winning_numbers: list[int], card_numbers: list[int]
    ) -> None:
        self.id = id
        self.winning_numbers = winning_numbers
        self.card_numbers = card_numbers

    @property
    def matches(self):
        return [n for n in self.card_numbers if n in self.winning_numbers]

    @classmethod
    def from_record(cls, line: str) -> "Scratchcard":
        card_details, card_contents = line.strip().split(": ")

        _, id = card_details.split()
        id = int(id)

        winning_numbers, card_numbers = card_contents.strip().split(" | ")
        winning_numbers = [int(n) for n in winning_numbers.split()]
        card_numbers = [int(n) for n in card_numbers.split()]

        return cls(id=id, winning_numbers=winning_numbers, card_numbers=card_numbers)


def calculate_points(num_matches: int) -> int:
    return int(math.pow(2, num_matches - 1))


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        lines = f.readlines()

    total_points = 0

    cards: dict[int, int] = defaultdict(lambda: 1)

    for line in lines:
        card = Scratchcard.from_record(line)
        num_matches = len(card.matches)

        total_points += calculate_points(num_matches)

        for _ in range(cards[card.id]):
            for i in range(card.id+1, card.id+1+num_matches):
                print(f"inc card{i} from {cards[i]} to {cards[i]+1}")
                cards[i] += 1
            print()

    # print(total_points)
    print(cards)
    print(sum(cards.values()))
