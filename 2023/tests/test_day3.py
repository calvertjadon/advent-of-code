import pytest

from aoc2023.day3 import Dir, Point, find_symbols_adjacent_to_point


def test_directions():
    samples = [
        """\
..!......
...123...""".splitlines(),
        """\
...!.....
...123...""".splitlines(),
        """\
....!....
...123...""".splitlines(),
        """\
.....!...
...123...""".splitlines(),
        """\
......!..
...123...""".splitlines(),
"...123!..".splitlines(),
        """\
...123...
......!..""".splitlines(),
        """\
...123...
.....!...""".splitlines(),
        """\
...123...
....!....""".splitlines(),
        """\
...123...
...!.....""".splitlines(),
        """\
...123...
..!......""".splitlines(),
"..!123...".splitlines(),
    ]

    for sample_input in samples:
        points = []

        for y in range(len(sample_input)):
            for x in range(len(sample_input[y])):
                if sample_input[y][x].isdigit():
                    points.append(Point(x, y))

        print("\n", sample_input)
        print(points)

        assert any(find_symbols_adjacent_to_point(point, sample_input) for point in points) == True
