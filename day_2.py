USE_TEST_INPUT = False

_day = __file__[-4]
_file_name = f"\\test_input_{_day}.txt" if USE_TEST_INPUT else f"\\input_{_day}.txt"

with open(__file__.rsplit("\\", 1)[0] + _file_name, "r") as file:
    puzzle_input = tuple(tuple(int(i) for i in report.split(" ")) for report in file.read().split("\n"))


def main(report):
    last_value = report[0]
    report_is_ascending = last_value < report[1]
    skip = False
    for value in report[1:]:

        if (not 1 <= abs(value - last_value) <= 3) or \
                (report_is_ascending and value < last_value) or \
                (not report_is_ascending and value > last_value):

            skip = True
            break

        last_value = value

    return 0 if skip else 1


def part_one():
    answer = 0

    for report in puzzle_input:
        answer += main(report)

    return answer


def part_two():
    answer = 0

    for report in puzzle_input:

        if main(report) == 1:
            answer += 1
            continue

        for i in range(len(report)):
            if main(report[:i] + report[i+1:]) == 1:    # uses the whole report, except for the i-th element
                answer += 1
                break

    return answer


print(part_one())
print(part_two())
