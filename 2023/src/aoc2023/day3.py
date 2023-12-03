import sys


def is_symbol(c: str) -> bool:
    return not c.isalnum() and c != "."


if __name__ == "__main__":
    #    sample_input = """\
    # 467..114..
    # ...*......
    # ..35..633.
    # ......#...
    # 617*......
    # .....+.58.
    # ..592.....
    # ......755.
    # ...$.*....
    # .664.598..""".splitlines()

    with open(sys.argv[1], "r") as f:
        sample_input = f.readlines()

    total = 0
    for i, line in enumerate(sample_input):
        n = ""
        is_part_number = False
        for j, char in enumerate(line):
            if char.isdigit():
                n += char

                # check if n is a part number
                # check left
                if (
                    j > 0
                    and not sample_input[i][j - 1].isdigit()
                    and sample_input[i][j - 1] != "."
                ):
                    is_part_number = True
                    continue

                # check up left diag
                if (
                    j > 0
                    and i > 0
                    and not sample_input[i - 1][j - 1].isdigit()
                    and sample_input[i - 1][j - 1] != "."
                ):
                    is_part_number = True
                    continue

                # check up
                if (
                    i > 0
                    and not sample_input[i - 1][j].isdigit()
                    and sample_input[i - 1][j] != "."
                ):
                    is_part_number = True
                    continue

                # check up right diag
                if (
                    j < len(line) - 2
                    and i > 0
                    and not sample_input[i - 1][j + 1].isdigit()
                    and sample_input[i - 1][j + 1] != "."
                ):
                    is_part_number = True
                    continue

                # check right
                if (
                    j < len(line) - 2
                    and not sample_input[i][j + 1].isdigit()
                    and sample_input[i][j + 1] != "."
                ):
                    is_part_number = True
                    continue

                # check down right diag
                if (
                    j < len(line) - 2
                    and i < len(sample_input) - 2
                    and not sample_input[i + 1][j + 1].isdigit()
                    and sample_input[i + 1][j + 1] != "."
                ):
                    is_part_number = True
                    continue

                # check down
                if (
                    i < len(sample_input) - 2
                    and not sample_input[i + 1][j].isdigit()
                    and sample_input[i + 1][j] != "."
                ):
                    is_part_number = True
                    continue

                # check down left diag
                if (
                    j > 0
                    and i < len(sample_input) - 2
                    and not sample_input[i + 1][j - 1].isdigit()
                    and sample_input[i + 1][j - 1] != "."
                ):
                    is_part_number = True
                    continue
            else:
                if is_part_number:
                    print(n)
                    total += int(n)
                    n = ""
                    is_part_number = False

    print(total)
