USE_TEST_INPUT = False

GRID_SIZE = 71
DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))

_day = __file__.rsplit("\\", 1)[1][4:-3]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    puzzle_input = tuple((int(x), int(y)) for y, x in (line.split(",")for line in file.read().split("\n")))


def is_valid(x, y):
    return True if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE else False


def part_one(byte_count=1024):
    current_positions = {(0, 0)}
    possible_positions, corrupted = set(), set()
    answer = 0
    for x, y in puzzle_input[:byte_count]:
        corrupted.add((x, y))
    while True:
        answer += 1
        for position in current_positions:
            for direction in DIRECTIONS:
                row, col = position[0] + direction[0], position[1] + direction[1]
                if row == GRID_SIZE-1 and col == GRID_SIZE-1:
                    return answer

                if is_valid(row, col) and (row, col) not in corrupted:
                    possible_positions.add((row, col))

        current_positions = possible_positions
        possible_positions = set()


def part_two(start_byte=1024):
    corrupted = set()
    for x, y in puzzle_input[:start_byte]:
        corrupted.add((x, y))
    while True:
        start_byte += 1
        current_positions = {(0, 0)}
        possible_positions, visited = set(), set()
        corrupted.add(puzzle_input[start_byte])
        loop = True
        while loop:
            for position in current_positions:
                for direction in DIRECTIONS:
                    row, col = position[0] + direction[0], position[1] + direction[1]
                    new_position = (row, col)
                    if is_valid(row, col) and new_position not in corrupted and new_position not in visited:
                        possible_positions.add(new_position)

                    if row == GRID_SIZE - 1 and col == GRID_SIZE - 1:
                        loop = False
                        break

            current_positions = possible_positions
            visited.update(possible_positions)
            if len(current_positions) == 0:
                answer = puzzle_input[start_byte]
                return f"{answer[1]},{answer[0]}"
            possible_positions = set()


print(part_one())
print(part_two())
