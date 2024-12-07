def load_input(test: bool = True) -> str:
    with open(("test.txt" if test else "input.txt"), "r", encoding="utf-8") as file:
        return file.read()
