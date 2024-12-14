import re
from math import prod
from itertools import count

USE_TEST_INPUT = False

_day = __file__.rsplit("\\", 1)[1][4:-3]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

ROW_COUNT, COL_COUNT = 103, 101
BASE_TIME = 100

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    puzzle_input = tuple(tuple(map(int, re.findall(r"(-?\d+)", instruction)))for instruction in file.read().split("\n"))


def part_one():
    answer = [0]*4
    for robot in puzzle_input:
        x = (robot[0] + BASE_TIME*robot[2]) % COL_COUNT
        y = (robot[1] + BASE_TIME*robot[3]) % ROW_COUNT

        quadrant = 0
        if x == COL_COUNT//2 or y == ROW_COUNT//2:
            continue
        if x > COL_COUNT/2:
            quadrant += 1
        if y > ROW_COUNT/2:
            quadrant += 2
        answer[quadrant] += 1

    return prod(answer)


def part_two():
    for time in count():
        character_counter = {k: 0 for k in range(ROW_COUNT)}
        visualisation = [["."] * COL_COUNT for _ in range(ROW_COUNT)]
        for robot in puzzle_input:
            x = (robot[0] + time*robot[2]) % COL_COUNT
            y = (robot[1] + time*robot[3]) % ROW_COUNT
            visualisation[y][x] = ["#"]
            character_counter[y] += 1

        if max(val for val in character_counter.values()) < 30:
            continue
        print(time)
        for line in visualisation:
            s = ""
            for char in line:
                s += char[0]
            print(s)
        print("\n\n\n")


print(part_one())
print(part_two())
