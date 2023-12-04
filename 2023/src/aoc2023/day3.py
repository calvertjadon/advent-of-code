from collections import defaultdict
import math
import sys

from dataclasses import dataclass
from enum import Enum


class Dir(tuple, Enum):
    LEFT        =   (-1,  0)
    UP_LEFT     =   (-1, -1)
    UP          =   ( 0, -1)
    UP_RIGHT    =   ( 1, -1)
    RIGHT       =   ( 1,  0)
    RIGHT_DOWN  =   ( 1,  1)
    DOWN        =   ( 0,  1)
    DOWN_LEFT   =   (-1,  1)

@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash((self.x, self.y))

def is_symbol(c: str) -> bool:
    return not c.isalnum() and c != "."


def find_symbols_adjacent_to_point(p: Point, lines: list[str]) -> list[Point]:
    adjacent = []

    for x_offset, y_offset in Dir:

        curr = Point(p.x + x_offset, p.y + y_offset)
        if 0 <= curr.y < len(lines) and 0 <= curr.x < len(lines[curr.y]) and is_symbol(char_at_pos(curr, lines)):
            adjacent.append(curr)

    return adjacent

def char_at_pos(p: Point, lines: list[str]) -> str:
    return lines[p.y][p.x]


if __name__ == "__main__":
    with open(sys.argv[1], "r") as f:
        lines = f.read().strip().splitlines()

    part_numbers = []
    gear_ratio_candiates: dict[Point, list[int]] = defaultdict(list)

    for i, line in enumerate(lines):
        line = line.strip() + "."
        part_number_digits: list[str] = []
        adjacent_symbol_positions: set[Point] = set()

        for j, char in enumerate(line):

            if char.isdigit():
                part_number_digits.append(char)

                for p in find_symbols_adjacent_to_point(Point(j, i), lines):
                    adjacent_symbol_positions.add(p)

            else:
                if len(adjacent_symbol_positions) > 0:

                    part_number = int("".join(part_number_digits))
                    part_numbers.append(part_number)

                    for symbol_pos in adjacent_symbol_positions:
                        if char_at_pos(symbol_pos, lines) == "*":
                            gear_ratio_candiates[symbol_pos].append(part_number)

                part_number_digits = []
                adjacent_symbol_positions = set()

    gear_ratio = 0
    for symbol_pos, gears in gear_ratio_candiates.items():
        if len(gears) == 2:
            gear_ratio += math.prod(gears)

    print(f"part number sum: {sum(part_numbers)}")
    print(f"gear_ratio: {gear_ratio}")

