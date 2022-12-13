from typing import AnyStr, List
from pprint import pprint


def read_input_file(file_path: AnyStr) -> List[AnyStr]:
    """Reads input file as a list"""
    print(f"Reading input file '{file_path}' to a list...")
    with open(file_path, "r") as f:
        return [x.strip() for x in f.read().split("\n")]


def main():
    raw_lines_list = read_input_file(file_path="josh_22/input_files/day12.txt")
    grid = [[char for char in x] for x in raw_lines_list]
    
    """
    [
        ['S', 'a', 'b', 'q', 'p', 'o', 'n', 'm'],
        ['a', 'b', 'c', 'r', 'y', 'x', 'x', 'l'],
        ['a', 'c', 'c', 's', 'z', 'E', 'x', 'k'],
        ['a', 'c', 'c', 't', 'u', 'v', 'w', 'j'],
        ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i']
    ]
    """
    for y in range(0, len(grid)):
        for x in range(0, len(grid[0])):
            pprint(grid[y][x])


if __name__ == "__main__":
    main()
