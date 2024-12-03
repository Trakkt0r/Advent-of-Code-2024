import re

USE_TEST_INPUT = False

PATTERN_ONE = r"mul\(\d{1,3},\d{1,3}\)"
PATTERN_TWO = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
EXTRACT_NUMBERS_PATTERN = r"mul\((\d+),(\d+)\)"

_day = __file__[-4]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    puzzle_input = file.read()


def part_one():
    answer = 0

    for instruction in re.findall(PATTERN_ONE, puzzle_input):
        x_y = re.match(EXTRACT_NUMBERS_PATTERN, instruction).groups()
        answer += int(x_y[0]) * int(x_y[1])

    return answer


def part_two():
    answer = 0
    can_multiply = True

    for instruction in re.findall(PATTERN_TWO, puzzle_input):

        if instruction == "do()":
            can_multiply = True
            continue

        elif instruction == "don't()":
            can_multiply = False
            continue

        if not can_multiply:
            continue

        x_y = re.match(EXTRACT_NUMBERS_PATTERN, instruction).groups()
        answer += int(x_y[0]) * int(x_y[1])

    return answer


print(part_one())
print(part_two())
