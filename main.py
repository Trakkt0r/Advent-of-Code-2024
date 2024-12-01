USE_TEST_INPUT = False

_file_name = "\\test_input.txt" if USE_TEST_INPUT else "\\input.txt"


def process_input(raw_input):
    output = [[], []]

    for line in raw_input:
        line_split = line.split("   ")
        for i, output_part in enumerate(output):
            output_part.append(line_split[i])

    for i, output_part in enumerate(output):
        output_part.sort()

    return output


with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    puzzle_input = process_input(file.read().split("\n"))


def part_one():
    answer = 0

    for i, element in enumerate(puzzle_input[0]):
        answer += abs(int(element) - int(puzzle_input[1][i]))

    return answer


def part_two():
    answer = 0

    for i, element in enumerate(puzzle_input[0]):
        answer += int(element) * puzzle_input[1].count(element)

    return answer


print(part_one())
print(part_two())
