from math import log10
from functools import cache

USE_TEST_INPUT = False

_day = __file__.rsplit("\\", 1)[1][4:-3]

_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    start_rocks = tuple(int(rock) for rock in file.read().split(" "))


@cache
def apply_rules(rock, blink_limit, blink=0):
    if blink == blink_limit:
        return 1
    if rock == 0:
        return apply_rules(1, blink_limit, blink+1)
    digits = int(log10(rock)) + 1
    if digits % 2 == 0:
        rock1, rock2 = divmod(rock, 10**(digits/2))
        return apply_rules(rock1, blink_limit, blink+1) + apply_rules(rock2, blink_limit, blink+1)
    return apply_rules(rock*2024, blink_limit, blink+1)


def run(blink_limit):
    answer = 0
    for rock in start_rocks:
        answer += apply_rules(rock, blink_limit)

    return answer


print(run(25))
print(run(75))
