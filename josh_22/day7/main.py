from typing import AnyStr, List
import os


def read_input_file(file_path: AnyStr) -> List[AnyStr]:
    """Reads input file as a list"""
    print(f"Reading input file '{file_path}' to a list...")
    with open(file_path, "r") as f:
        return [line.rstrip() for line in f.readlines()]


def main():
    input_lines = read_input_file(file_path="josh_22/input_files/day7.txt")

    subdirectories = {}
    directory_sizes = {}

    for line in input_lines:
        if "$ cd " in line:
            destination_path = line.split(" ")[2]
            if destination_path == "/":
                current_directory = destination_path
            else:
                current_directory = os.path.normpath(
                    os.path.join(current_directory, destination_path)
                )
            if current_directory not in subdirectories:
                subdirectories[current_directory] = []
                directory_sizes[current_directory] = 0
        elif "dir " in line:
            new_subdir_name = line.split(" ")[1]
            subdirectories[current_directory].append(
                os.path.normpath(os.path.join(current_directory, new_subdir_name))
            )
        elif "$ ls" not in line:
            filesize = int(line.split(" ")[0])
            directory_sizes[current_directory] += filesize

    def compute_size(directory_name: str) -> int:
        directory_size = directory_sizes[directory_name]
        for subdirectory in subdirectories[directory_name]:
            if subdirectory in subdirectories:
                directory_size += compute_size(subdirectory)
        return directory_size

    # Part 1
    counter = 0
    for subdirectory in subdirectories:
        directory_size = compute_size(
            subdirectory,
        )
        if directory_size <= 100000:
            counter += directory_size
    print(counter)

    # Part 2
    total_space = 70000000
    space_required = 30000000
    space_used = compute_size("/")

    directory_to_delete = total_space
    for directory in directory_sizes:
        size = compute_size(directory)
        if (
            size >= space_required - (total_space - space_used)
            and size <= directory_to_delete
        ):
            directory_to_delete = size
    print(directory_to_delete)


if __name__ == "__main__":
    main()
