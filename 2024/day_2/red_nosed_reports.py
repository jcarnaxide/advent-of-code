from itertools import pairwise

def read_input_file():
    with open('input.txt', 'r') as file:
        return file.read()

def pythonify(raw_text: str):
    return [[int(num) for num in line.split(' ')] for line in raw_text.splitlines()]

def report_is_safe(report: list[int]):
    inc_or_dec = None
    for x, y in pairwise(report):
        if x == y:
            return False
        if inc_or_dec is None:
            if x < y:
                inc_or_dec = 'inc'
            else:
                inc_or_dec = 'dec'
        else:
            if inc_or_dec == 'inc' and x > y:
                return False
            elif inc_or_dec == 'dec' and x < y:
                return False
        if abs(x-y) > 3:
            return False
    return True

def report_is_safish(report: list[int]):
    if report_is_safe(report):
        return True
    for i in range(len(report)):
        if report_is_safe([x for j, x in enumerate(report) if j != i]):
            return True

if __name__ == '__main__':
    print('Advent Day 2')
    raw_text = read_input_file()
    # print(raw_text)
    reports = pythonify(raw_text)
    # print(reports)
    safe_report_count = 0
    safish_report_count = 0
    for report in reports:
        if report_is_safe(report):
            safe_report_count += 1
        if report_is_safish(report):
            safish_report_count += 1
    # print(safe_report_count)
    print(safish_report_count)
