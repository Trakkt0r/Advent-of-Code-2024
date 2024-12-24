USE_TEST_INPUT = False
DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))

_day = __file__.rsplit("\\", 1)[1][4:-3]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    puzzle_input = tuple(tuple(int(height) for height in list(line)) for line in file.read().split("\n"))
    max_row, max_col = len(puzzle_input), len(puzzle_input[0])


def is_valid(row, col):
    return 0 <= row < max_row and 0 <= col < max_col


def find_next(row, col, visited, val, find_unique=False):
    answer = 0
    if val == 9 and (row, col) not in visited:
        if find_unique:
            visited.add((row, col))
        return 1

    for direction in DIRECTIONS:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if is_valid(new_row, new_col) and puzzle_input[new_row][new_col] == val+1:
            answer += find_next(new_row, new_col, visited, val+1, find_unique)

    return answer


def run(find_unique):
    answer = 0
    for row, line in enumerate(puzzle_input):
        for col, value in enumerate(line):
            if value != 0:
                continue
            answer += find_next(row, col, set(), 0, find_unique)

    return answer


print(run(True))        # Represents part 1
print(run(False))       # Represents part 2
