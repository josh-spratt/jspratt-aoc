from typing import List, AnyStr
from pprint import pprint


class Instruction:
    def __init__(self, instruction_type=None, value=0):
        self.instruction_type = instruction_type
        self.value = value


def read_input_file(file_path: str) -> List[AnyStr]:
    """Reads input file as a list"""
    print(f"Reading input file '{file_path}' to a list...")
    with open(file_path, "r") as f:
        return [line.rstrip() for line in f.readlines()]


def main():
    program_lines = read_input_file(file_path="josh_22/input_files/day10.txt")

    instructions = []
    for program_line in program_lines:
        instruction_type = program_line.split(" ")[0]
        if len(program_line.split(" ")) == 2:
            value = int(program_line.split(" ")[1])
            instruction = Instruction(instruction_type, value)
        else:
            instruction = Instruction(instruction_type, 0)
        instructions.append(instruction)

    x = 1
    cycle = 0
    for instruction in instructions:
        if instruction.instruction_type == "noop":
            pass
        elif instruction.instruction_type == "addx":
            pass


if __name__ == "__main__":
    main()
