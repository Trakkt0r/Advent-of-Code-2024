import numpy as np

USE_TEST_INPUT = False

_day = __file__[-4]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    puzzle_input = {tuple(map(int, v.split(" "))): int(k)
                    for k, v in (i.split(": ")
                    for i in [line for line in file.read().split("\n")])}


# given a number, it uses the binary/ternary to map each operator
# 0 = add, 1 = mul, (2 = concat)
def solution(part):
    base = part + 1     # yes, that's the only difference between pt1 and 2
    answer = 0

    for numbers, goal in puzzle_input.items():
        for setter in range(base**(len(numbers)-1)):
            result = numbers[0]

            for i, value in enumerate(np.base_repr(setter, base=base).zfill(len(numbers)-1)):
                if value == "0":
                    result += numbers[i + 1]
                elif value == "1":
                    result *= numbers[i + 1]
                else:
                    result = int(str(result) + str(numbers[i+1]))

            if result == goal:
                answer += result
                break

    return answer


print(solution(1))
print(solution(2))
