from functools import reduce
import operator
import re

def load_input() -> str:
    with open("input.txt", "r", encoding="utf-8") as file:
        return file.read()

def find_valid_muls(raw_text: str) -> tuple[int,int]:
    matches = re.finditer(r"mul\((-?\d+),(-?\d+)\)", raw_text)
    return [(int(match.group(1)), int(match.group(2))) for match in matches]

def find_patterns(raw_text: str):
    matches = re.finditer(r"(mul)\((-?\d+),(-?\d+)\)|(do)\(\)|(don't)\(\)", raw_text)
    return_val = []
    for match in matches:
        operation = match.group(1) or match.group(4) or match.group(5)
        # print(operation)
        return_val.append({
            "operation": operation
        })
        if operation == "mul":
            return_val[-1].update({
                "x": int(match.group(2)),
                "y": int(match.group(3)),
            })
    return return_val

def part_1():
    raw_text = load_input()
    # print(raw_text)
    valid_muls = find_valid_muls(raw_text)
    # print(valid_muls)
    products = list(map(operator.mul, *(zip(*valid_muls))))
    # print(products)
    summed_muls = sum(products)
    print(summed_muls)

def part_2():
    raw_text = load_input()
    patterns = find_patterns(raw_text)
    # print(patterns)
    mul_enabled = True
    summed_enabled_muls = 0
    for pattern in patterns:
        match pattern["operation"]:
            case "mul":
                if mul_enabled:
                    summed_enabled_muls += pattern["x"] * pattern["y"]
            case "do":
                mul_enabled = True
            case "don't":
                mul_enabled = False
    print(summed_enabled_muls)

if __name__ == "__main__":
    print("Advent of Code 2024 - Day 3")
    # part_1()
    part_2()
