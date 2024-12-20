import numpy as np
import re

USE_TEST_INPUT = False

_day = __file__.rsplit("\\", 1)[1][4:-3]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    raw_input = tuple(equation for equation in file.read().split("\n\n"))
    processed_input_1 = tuple(tuple(map(int, re.findall(r"(\d+)", equation))) for equation in raw_input)
    processed_input_2 = tuple(
        tuple(int(x) if i < 4 else 1e13 + int(x)
              for i, x in enumerate(re.findall(r"(\d+)", equation))
              ) for equation in raw_input)


# Uses solving systems of linear equations via matrices
# Puzzle input always has a non-zero determinant -> there's always 1 solution
def solve_equation(coefficient_matrix, constant_matrix):
    solution = np.linalg.inv(coefficient_matrix) @ constant_matrix      # @ = Matrix multiplication

    A, B = solution.item(0), solution.item(1)

    # Floating point error correction
    rounded_a, rounded_b = round(A), round(B)
    if abs(A - rounded_a) < 0.0001 and abs(B - rounded_b) < 0.0001:
        return 3 * rounded_a + rounded_b
    return 0


def run(processed_input):
    answer = 0
    for line in processed_input:
        A_x, A_y, B_x, B_y, P_x, P_y = line
        coefficient_matrix = np.array([[A_x, B_x], [A_y, B_y]])
        constant_matrix = np.array([[P_x], [P_y]])
        answer += solve_equation(coefficient_matrix, constant_matrix)
    return answer


print(run(processed_input_1))
print(run(processed_input_2))
