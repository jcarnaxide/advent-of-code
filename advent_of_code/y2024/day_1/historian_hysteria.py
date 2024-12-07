from collections import Counter

if __name__ == "__main__":
    print("Advent Day 1")
    with open('input.txt', 'r') as file:
        raw_text = file.read()
    # print(raw_text)
    lines = raw_text.splitlines()
    # print(lines)
    tokenized_lines = [line.split("   ") for line in lines]
    # print(tokenized_lines)
    left, right = zip(*tokenized_lines)
    left_ints = [int(x) for x in left]
    right_ints = [int(x) for x in right]
    # print(left)
    distance = 0
    for l, r in zip(sorted(left_ints), sorted(right_ints)):
        distance += abs(l-r)
    # print(distance)

    left_counter = Counter(left_ints)
    right_counter = Counter(right_ints)
    similarity = 0
    for num, count in left_counter.items():
        if num in right_counter:
            similarity += count * num * right_counter[num]
    print(similarity)
