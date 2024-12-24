from itertools import product

USE_TEST_INPUT = False
DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))

_day = __file__.rsplit("\\", 1)[1][4:-3]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    puzzle_input = tuple(line for line in file.read().split("\n"))

max_row = len(puzzle_input)
max_col = len(puzzle_input[0])


def is_valid(row, col):
    if 0 <= row < max_row and 0 <= col < max_col:
        return True
    return False


def count_bends(start_row, start_col, shape):
    bends = 0
    for dr, dc in product((-1, 1), repeat=2):
        new_row, new_col = start_row+dr, start_col+dc
        if not is_valid(new_row, new_col) or puzzle_input[new_row][new_col] == shape:
            continue

        if puzzle_input[new_row][start_col] == shape and puzzle_input[start_row][new_col] == shape:
            bends += 1

    return bends


def part_one_recursion(row, col, value, visited: set):
    visited.add((row, col))
    perimeter = 0

    for direction in DIRECTIONS:
        new_row = row + direction[0]
        new_col = col + direction[1]
        if (new_row, new_col) in visited:
            continue

        if is_valid(new_row, new_col) and value == puzzle_input[new_row][new_col]:
            perimeter += part_one_recursion(new_row, new_col, value, visited)[0]
        else:
            perimeter += 1

    return perimeter, visited


def part_two_recursion(start_row, start_col, shape, visited):
    vertices = count_bends(start_row, start_col, shape)
    visited.add((start_row, start_col))
    neighbor_count, v_count, h_count = 0, 0, 0
    for direction in DIRECTIONS:
        row = start_row+direction[0]
        col = start_col+direction[1]

        if is_valid(row, col) and puzzle_input[row][col] == shape:
            neighbor_count += 1
            v_count += 1 if col == start_col else 0
            h_count += 1 if row == start_row else 0
            if (row, col) in visited:
                continue
            add_to_ans, visited = part_two_recursion(row, col, shape, visited)
            vertices += add_to_ans

    if neighbor_count == 0:
        vertices = 4
    elif neighbor_count == 1:
        vertices += 2
    if v_count == h_count == 1:
        vertices += 1

    return vertices, visited


def part_one():
    answer = 0
    visited = set()
    for row, line in enumerate(puzzle_input):
        for col, value in enumerate(line):
            if (row, col) in visited:
                continue

            perimeter, area_set = part_one_recursion(row, col, puzzle_input[row][col], set())
            visited.update(area_set)
            answer += len(area_set) * perimeter

    return answer


def part_two():
    answer = 0
    visited = set()
    for row, line in enumerate(puzzle_input):
        for col, value in enumerate(line):
            if (row, col) in visited:
                continue

            vertices, area_set = part_two_recursion(row, col, puzzle_input[row][col], set())
            visited.update(area_set)
            answer += len(area_set) * vertices

    return answer


print(part_one())
print(part_two())
