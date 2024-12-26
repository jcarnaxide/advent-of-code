import os

def get_local_file_path(script_file, relative_path):
    script_dir = os.path.dirname(os.path.abspath(script_file))
    return os.path.join(script_dir, relative_path)

def load_file(script_file, test: bool = True) -> str:
    file_path = get_local_file_path(script_file, ("test.txt" if test else "input.txt"))
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
