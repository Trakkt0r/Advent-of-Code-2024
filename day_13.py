import numpy as np
import re
from timeit import timeit

USE_TEST_INPUT = False

_day = __file__.rsplit("\\", 1)[1][4:-3]

_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"


def part_two_processor(equation):
    result = 6*[None]                   # Pre-allocates the size to 6
    for i, value in enumerate(re.findall(r"[+=](\d+)", equation)):
        if i < 4:
            result[i] = int(value)
        else:
            result[i] = 10000000000000 + int(value)
    return result


with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    raw_input = tuple(equation for equation in file.read().split("\n\n"))
    processed_input_1 = tuple(tuple(map(int, re.findall(r"[+=](\d+)", equation))) for equation in raw_input)
    processed_input_2 = tuple(tuple(map(part_two_processor, raw_input)))


# Uses solving systems of linear equations via matrices
# Puzzle input always has a non-zero determinant -> there's always 1 solution
def solve_equation(coefficient_matrix, constant_matrix):
    solution = coefficient_matrix.I * constant_matrix

    A, B = solution.item(0), solution.item(1)

    # floating point error mitigation
    if np.abs(A - round(A)) < 0.0001 and np.abs(B - round(B)) < 0.0001:
        return 3 * round(A) + round(B)
    return 0


def run(processed_input=processed_input_2):
    answer = 0
    for line in processed_input:
        A_x, A_y, B_x, B_y, P_x, P_y = line
        coefficient_matrix = np.matrix([[A_x, B_x], [A_y, B_y]])
        constant_matrix = np.matrix([[P_x], [P_y]])
        answer += solve_equation(coefficient_matrix, constant_matrix)
    return answer


def div(a=50445156, b=28451):
    return a/b

print(timeit(div, number=10**6))