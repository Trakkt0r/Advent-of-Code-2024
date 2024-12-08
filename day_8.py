import itertools
import numpy as np

USE_TEST_INPUT = False

_day = __file__[-4]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    puzzle_input = file.read().split("\n")

max_size = len(puzzle_input)-1

antennas = {}

for row, line in enumerate(puzzle_input):
    for col, char in enumerate(line):
        if char == ".":
            continue

        if antennas.get(char) is None:
            antennas[char] = np.array([row, col])
        else:
            antennas[char] = np.vstack((antennas[char], [row, col]))


def part_one():
    answer = set()

    for freq, positions in antennas.items():
        for pair in itertools.permutations(positions, 2):
            value = 2*pair[0] - pair[1]

            if np.all((value >= 0) & (value <= max_size)):
                answer.add((value[0], value[1]))

    return len(answer)


def part_two():
    answer = set()

    for freq, positions in antennas.items():
        for pair in itertools.permutations(positions, 2):
            delta = pair[1] - pair[0]
            for i in itertools.count(1):
                value = pair[0] + i*delta
                if np.all((value >= 0) & (value <= max_size)):
                    answer.add((value[0], value[1]))
                else:
                    break

    return len(answer)


print(part_one())
print(part_two())
