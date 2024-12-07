import itertools

USE_TEST_INPUT = False

_day = __file__[-4]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    raw_rules, raw_outputs = file.read().split("\n\n")
    rules = tuple(raw_rules.split("\n"))
    outputs = [list(map(int, x.split(","))) for x in raw_outputs.split("\n")]


def part_one():
    answer = 0

    for output in outputs:
        is_valid = True

        for combination in itertools.combinations(output, 2):
            if f"{combination[1]}|{combination[0]}" in rules:
                is_valid = False
                break

        answer += output[len(output)//2] if is_valid else 0

    return answer


def part_two():
    answer = 0

    for output in outputs:
        sorted_output = output.copy()
        while True:
            for combination in itertools.combinations(sorted_output, 2):
                a, b = combination[0], combination[1]
                if f"{b}|{a}" in rules:
                    a_index = sorted_output.index(a)
                    b_index = sorted_output.index(b)
                    sorted_output[a_index] = b
                    sorted_output[b_index] = a
                    break

            is_valid = True

            for combination in itertools.combinations(sorted_output, 2):
                if f"{combination[1]}|{combination[0]}" in rules:
                    is_valid = False
                    break

            if is_valid:
                break

        answer += sorted_output[len(sorted_output) // 2] if sorted_output != output else 0

    return answer


print(part_one())
print(part_two())
