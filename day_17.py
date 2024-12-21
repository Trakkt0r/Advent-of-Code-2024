import re

USE_TEST_INPUT = False

_day = __file__.rsplit("\\", 1)[1][4:-3]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"


def process_input(line):
    if line[0] == "R":
        return int(line[12:])
    return tuple(map(int, re.findall(r"\d+", line)))


with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    processed_input = [process_input(line) for line in file.read().split("\n") if line != ""]


def combo(operand, a, b, c):
    match operand:
        case 4:
            return a
        case 5:
            return b
        case 6:
            return c
    return operand


def part_one():
    a, b, c, instructions = processed_input
    pointer = 0
    answer = ""
    while pointer < len(instructions)-1:
        opcode, operand = instructions[pointer:pointer+2]
        match opcode:
            case 0:  # adv
                a = a // 2 ** combo(operand, a, b, c)
            case 1:  # bxl
                b = b ^ operand
            case 2:  # bst
                b = combo(operand, a, b, c) % 8
            case 3:  # jnz
                if a != 0:
                    pointer = operand
                    continue
            case 4:  # bxc
                b = b ^ c
            case 5:  # out
                answer += f"{combo(operand, a, b, c) % 8},"
            case 6:  # bdv
                b = a // 2 ** combo(operand, a, b, c)
            case 7:  # cdv
                c = a // 2 ** combo(operand, a, b, c)
        pointer += 2
    return answer[:-1]


print(part_one())
