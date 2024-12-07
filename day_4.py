import itertools

USE_TEST_INPUT = False

_day = __file__[-4]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    puzzle_input = tuple(file.read().split("\n"))

row_limit = len(puzzle_input) - 1
col_limit = len(puzzle_input[0]) - 1

other_letter = {"M": "S", "S": "M", "X": None, "A": None}

directions = tuple(
    tuple((n * x, n * y) for n in range(1, 4))
    for x, y in itertools.product({-1, 0, 1}, repeat=2)
    if (x, y) != (0, 0)
)


def part_one():
    answer = 0

    for row, line in enumerate(puzzle_input):
        for col, letter in enumerate(line):
            if letter != "X":
                continue

            for direction in directions:
                max_row, max_col = row + direction[2][0], col + direction[2][1]
                if not (0 <= max_row <= row_limit and 0 <= max_col <= col_limit):
                    continue

                is_xmas = True

                # cleaner way of doing if pos + dir[0] == M and pos + dir[1] == A and ...
                for k, v in {"M": 0, "A": 1, "S": 2}.items():
                    if puzzle_input[row + direction[v][0]][col + direction[v][1]] != k:
                        is_xmas = False
                        break

                if is_xmas:
                    answer += 1

    return answer


def part_two():
    answer = 0

    for row, line in enumerate(puzzle_input):
        for col, letter in enumerate(line):
            if letter != "A":
                continue

            if row == 0 or row == row_limit or col == 0 or col == col_limit:
                continue

            if puzzle_input[row + 1][col + 1] == other_letter[puzzle_input[row - 1][col - 1]] \
                    and puzzle_input[row + 1][col - 1] == other_letter[puzzle_input[row - 1][col + 1]]:
                answer += 1

    return answer


print(part_one())
print(part_two())
