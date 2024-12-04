def load_input() -> str:
    with open("input.txt", "r", encoding="utf-8") as file:
        return file.read()

def get_columns_from_rows(rows):
    columns = list(zip(*rows))
    columns = ["".join(col) for col in columns]
    print(columns)
    return columns

def get_diagonals(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Store diagonals
    diagonals_tl_br = []  # Top-left to bottom-right
    diagonals_tr_bl = []  # Top-right to bottom-left

    # Extract top-left to bottom-right diagonals
    for d in range(rows + cols - 1):
        diagonal = []
        for i in range(rows):
            for j in range(cols):
                if i + j == d:  # Condition for the top-left to bottom-right diagonal
                    diagonal.append(matrix[i][j])
        if diagonal:
            diagonals_tl_br.append("".join(diagonal))

    # Extract top-right to bottom-left diagonals
    for d in range(-rows + 1, cols):
        diagonal = []
        for i in range(rows):
            for j in range(cols):
                if j - i == d:  # Condition for the top-right to bottom-left diagonal
                    diagonal.append(matrix[i][j])
        if diagonal:
            diagonals_tr_bl.append("".join(diagonal))

    return diagonals_tl_br, diagonals_tr_bl

def reverse_it(strings):
    return [s[::-1] for s in strings]

def part_1():
    print("Part 1")

    raw_text = load_input()
    # print(raw_text)
    
    rows = raw_text.splitlines()
    print(rows)

    columns = get_columns_from_rows(rows)

    diagonals_tl_br, diagonals_tr_bl = get_diagonals(rows)
    print(diagonals_tl_br)
    print(diagonals_tr_bl)

    xmas_count = 0
    iterators_to_check = [
        rows,
        columns,
        diagonals_tl_br,
        diagonals_tr_bl,
    ]
    reversed_iterators_to_check = [reverse_it(i) for i in iterators_to_check]
    iterators_to_check.extend(reversed_iterators_to_check)

    for iterator in iterators_to_check:
        for string in iterator:
            xmas_count += string.count("XMAS")
    print(xmas_count)


def part_2():
    print("Part 2")
    raw_text = load_input()
    matrix = [[*line] for line in raw_text.splitlines()]
    # print(matrix)
    rows = len(matrix)
    cols = len(matrix[0])
    x_mas_count = 0
    for x in range(1, rows-1):
        for y in range(1, cols-1):
            if matrix[x][y] == "A":
                corners = matrix[x-1][y-1] + matrix[x-1][y+1] + matrix[x+1][y+1] + matrix[x+1][y-1]
                if corners in set(["MMSS", "SSMM", "MSSM", "SMMS"]):
                    x_mas_count += 1
    print(x_mas_count)


if __name__ == "__main__":
    print("Advent of Code( 2024 - Day 4")
    # part_1()
    part_2()
