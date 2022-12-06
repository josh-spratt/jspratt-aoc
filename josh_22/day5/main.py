from typing import AnyStr, List
from pprint import pprint
import re


def read_input_file(file_path: AnyStr) -> List[AnyStr]:
    """Reads input file as a list"""
    print(f"Reading input file '{file_path}' to a list...")
    with open(file_path, "r") as f:
        lines = [
            line.replace("                ", "[0] [0] [0] [0] ")
            .replace("     ", " [0] ")
            .strip()
            for line in f.readlines()
        ]
    return lines


def main():
    raw_lines = read_input_file(file_path="josh_22/input_files/day5.txt")
    cargo_stacks = []
    instructions = []
    for line in raw_lines:
        if "[" in line or "]" in line:
            cargo = line.replace("[", "").replace("]", "").replace("0", "").split(" ")
            cargo_stacks.append(cargo)
        elif "move" in line:
            instructions.append(
                [int(instruction) for instruction in re.findall(r"\d+", line)]
            )
    cargo_stacks = list(map(list, zip(*cargo_stacks)))
    new_stacks = []
    for stack in cargo_stacks:
        stack = [x for x in stack if x != ""]
        new_stacks.append(stack[::-1])

    # Part 1
    # for instruction in instructions:
    #     for _ in range(1, instruction[0] + 1):
    #         # print(_)
    #         move_from_stack = new_stacks[instruction[1] - 1]
    #         # print(move_from_stack)
    #         move_to_stack = new_stacks[instruction[2] - 1]
    #         # print(move_to_stack)
    #         move_to_stack.append(move_from_stack.pop())
    #         # print(move_from_stack)
    #         # print(move_to_stack)
    #     # pprint(new_stacks)

    # output = ""
    # for stack in new_stacks:
    #     output += stack[-1]

    # Part 2
    output = ""
    for instruction in instructions:
        move_from_stack = new_stacks[instruction[1] - 1]
        move_to_stack = new_stacks[instruction[2] - 1]
        items_to_move = move_from_stack[-instruction[0] :]
        move_to_stack.extend(items_to_move)
        for _ in range(1, instruction[0] + 1):
            move_from_stack.pop()

    for stack in new_stacks:
        output += stack[-1]
    print(output)


if __name__ == "__main__":
    main()
