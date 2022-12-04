from typing import AnyStr, List
from pprint import pprint


def read_input_file(file_path: AnyStr) -> List[AnyStr]:
    """Reads input file as a list"""
    print(f"Reading input file '{file_path}' to a list...")
    with open(file_path, "r") as f:
        return [line.rstrip().split(",") for line in f.readlines()]


def main():
    raw_input = read_input_file(file_path="josh_22/input_files/day4.txt")
    new_list = []
    for pair in raw_input:
        new_pair = []
        for x in pair:
            new_x = []
            for i in range(int(x.split("-")[0]), int(x.split("-")[1]) + 1):
                new_x.append(i)
            new_pair.append(new_x)
        new_list.append(new_pair)

    counter = 0
    for pair in new_list:
        if all(elem in pair[0] for elem in pair[1]) or all(
            elem in pair[1] for elem in pair[0]
        ):
            counter += 1
    print(counter)

    overlap_list = []
    for pair in new_list:
        overlap = [value for value in pair[0] if value in pair[1]]
        if len(overlap) != 0:
            overlap_list.append(len(overlap))
    print(len(overlap_list))


if __name__ == "__main__":
    main()
