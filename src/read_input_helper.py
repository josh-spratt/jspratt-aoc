def read_input_file(filepath: str) -> list:
    with open(filepath, "r") as f:
        return [int(x) for x in f.readlines()]