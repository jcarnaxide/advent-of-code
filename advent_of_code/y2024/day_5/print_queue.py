from collections import defaultdict
from itertools import pairwise

def load_input(test: bool = True) -> str:
    with open(("test.txt" if test else "input.txt"), "r", encoding="utf-8") as file:
        return file.read()

def get_rules_and_updates(raw_text: str):
    lines = raw_text.splitlines()
    print(lines)

    middle = lines.index("")

    rules = lines[:middle]
    rules = [rule.split("|") for rule in rules]
    rules = [[int(x), int(y)] for [x, y] in rules]
    print(rules)

    updates = lines[middle+1:]
    updates = [upd.split(",") for upd in updates]
    updates = [[int(page) for page in upd]for upd in updates]
    print(updates)
    
    return rules, updates

def get_flows(rules):
    flows = defaultdict(set)
    for rule in rules:
        flows[rule[0]].add(rule[1])
    return flows

def get_valid_invalid_updates(raw_text: str):
    rules, updates = get_rules_and_updates(raw_text)
    valid_updates = []
    invalid_updates = []
    flows = get_flows(rules)
    for upd in updates:
        valid = True
        for y, x in pairwise(reversed(upd)):
            if x in flows[y]:
                valid = False
                break
        if valid:
            valid_updates.append(upd)
        else:
            invalid_updates.append(upd)
    return valid_updates, invalid_updates

def get_sum_middles(updates):
    return sum([upd[len(upd)//2] for upd in updates])

def part_1(raw_text: str):
    valid_updates, _ = get_valid_invalid_updates(raw_text)
    print(get_sum_middles(valid_updates))

def part_2(raw_text: str):
    rules, _ = get_rules_and_updates(raw_text)
    flows = get_flows(rules)
    _, invalid_updates = get_valid_invalid_updates(raw_text)
    for upd in invalid_updates:
        print(f"before: {upd}")
        for _ in range(len(upd)):
            for j, i in pairwise(reversed(range(len(upd)))):
                if upd[i] in flows[upd[j]]:
                    upd[i], upd[j] = upd[j], upd[i]
        print(f"after: {upd}")
    print(get_sum_middles(invalid_updates))


if __name__ == "__main__":
    print("Advent of Code 2024 - Day 5")

    raw_text = load_input(False)
    print(raw_text)

    # part_1(raw_text)
    part_2(raw_text)
