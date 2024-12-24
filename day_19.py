from itertools import groupby
from functools import cache

USE_TEST_INPUT = False

_day = __file__.rsplit("\\", 1)[1][4:-3]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    input_patterns, designs = file.read().split("\n\n")
    input_patterns = sorted(input_patterns.split(", "), key=len)
    all_patterns = {length: tuple(group) for length, group in groupby(reversed(input_patterns), len)}
    all_lengths = all_patterns.keys()
    designs = designs.split("\n")[:-1]


@cache
def is_possible(design):
    design_length = len(design)
    if design_length == 0:
        return True

    for pattern_length in all_lengths:
        if design_length < pattern_length:
            continue

        if design[:pattern_length] in all_patterns[pattern_length]:
            if not is_possible(design[pattern_length:]):
                continue
            return True

    return False


@cache
def count_options(design):
    answer = 0
    design_length = len(design)

    if design_length == 0:
        return 1

    for pattern_length in all_lengths:
        if design_length < pattern_length:
            continue
        if design[:pattern_length] in all_patterns[pattern_length]:
            answer += count_options(design[pattern_length:])

    return answer


def part_one():
    answer = 0
    for design in designs:
        answer += is_possible(design)

    return answer


def part_two():
    answer = 0
    for i, design in enumerate(designs):
        answer += count_options(design)

    return answer


print(part_one())
print(part_two())
