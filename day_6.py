USE_TEST_INPUT = False

_day = __file__[-4]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    puzzle_input = [list(line) for line in file.read().split("\n")]

max_row = len(puzzle_input) - 1
max_col = len(puzzle_input[0]) - 1


def direction():
    while True:
        yield -1, 0
        yield 0, 1
        yield 1, 0
        yield 0, -1


def is_loop(replaced_row, replaced_col):
    start_symbol = puzzle_input[replaced_row][replaced_col]
    puzzle_input[replaced_row][replaced_col] = "#"
    past_states = set()

    direction_generator = direction()
    current_direction = next(direction_generator)

    row, col = 0, 0
    for i, line in enumerate(puzzle_input):
        if "^" in line:
            row, col = i, line.index("^")

    while True:
        next_row, next_col = row + current_direction[0], col + current_direction[1]
        current_state = (row, col, current_direction)

        if current_state in past_states:
            puzzle_input[replaced_row][replaced_col] = start_symbol
            return True

        # if the next value is outside the map, return
        if 0 > next_row or next_row > max_row or 0 > next_col or next_col > max_col:
            puzzle_input[replaced_row][replaced_col] = start_symbol
            return False

        past_states.add(current_state)

        if puzzle_input[next_row][next_col] == "#":
            current_direction = next(direction_generator)
            continue

        row = next_row
        col = next_col


def part_one():
    answer = 1      # accounts for the ^ being replaced to X

    row, col = 0, 0
    for i, line in enumerate(puzzle_input):
        if "^" in line:
            row, col = i, line.index("^")

    direction_generator = direction()
    current_direction = next(direction_generator)

    while True:
        next_row, next_col = row + current_direction[0], col + current_direction[1]

        if puzzle_input[row][col] == ".":
            answer += 1
            puzzle_input[row][col] = "X"

        # if the next value is outside the map, return
        if 0 > next_row or next_row > max_row or 0 > next_col or next_col > max_col:
            return answer

        if puzzle_input[next_row][next_col] == "#":
            current_direction = next(direction_generator)
            continue

        row = next_row
        col = next_col


def part_two():
    part_one()     # marks the path the guard normally walks on - anything else doesn't affect him if obstructed
    answer = 0

    for row, line in enumerate(puzzle_input):
        for col, char in enumerate(line):
            if char != "^" and char != "#" and is_loop(row, col):
                answer += 1

    return answer


print(part_one())
print(part_two())
