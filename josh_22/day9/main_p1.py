from typing import AnyStr, List
import json
import math


class Rope:
    def __init__(self, head=(0, 0), tail=(0, 0)):
        self.head = head
        self.tail = tail

    def move_head_coordinate(self, x_move, y_move):
        new_coordinate = tuple([self.head[0] + x_move, self.head[1] + y_move])
        return new_coordinate

    def check_tail_lag(self):
        return (self.head[0] - self.tail[0], self.head[1] - self.tail[1])

    def move_tail_coordinate(self, x_move, y_move):
        new_tail_coordinate = tuple([self.tail[0] + x_move, self.tail[1] + y_move])
        return new_tail_coordinate


class Instruction:
    def __init__(self, direction=None, value=0):
        self.direction = direction
        self.value = value

    def convert_instruction_to_coord(self):
        if self.direction == "R":
            x = 1
            y = 0
        elif self.direction == "D":
            x = 0
            y = -1
        elif self.direction == "L":
            x = -1
            y = 0
        elif self.direction == "U":
            x = 0
            y = 1
        return x, y


def read_input_file(file_path: AnyStr) -> List[AnyStr]:
    """Reads input file as a list"""
    print(f"Reading input file '{file_path}' to a list...")
    with open(file_path, "r") as f:
        return [line.rstrip() for line in f.readlines()]


def check_tail_lag(head, tail):
    return (head[0] - tail[0], head[1] - tail[1])


def main():
    raw_input = read_input_file(file_path="josh_22/input_files/day9.txt")
    rope_head = (0, 0)
    rope_tail = (0, 0)
    tail_coordinates = []
    tail_coordinates.append(rope_tail)
    print("\n")
    print("==========")

    for line in raw_input:
        direction = line.split(" ")[0]
        print(f"The direction the rope will move:\t{direction}")
        value = int(line.split(" ")[1])
        print(f"The distance the rope will move:\t{value}")

        for i in range(1, value + 1):
            instruction = Instruction(direction=direction, value=i)
            print(f"instruction: {instruction.convert_instruction_to_coord()}")
            rope_head = (
                rope_head[0] + instruction.convert_instruction_to_coord()[0],
                rope_head[1] + instruction.convert_instruction_to_coord()[1],
            )
            print(f"rope_head: {rope_head}")

            tail_lag = check_tail_lag(head=rope_head, tail=rope_tail)
            print(f"tail_lag: {tail_lag}")

            if tail_lag == (2, 0):
                rope_tail = (rope_tail[0] + 1, rope_tail[1] + 0)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)
            elif tail_lag == (0, 2):
                rope_tail = (rope_tail[0] + 0, rope_tail[1] + 1)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)
            elif tail_lag == (-2, 0):
                rope_tail = (rope_tail[0] - 1, rope_tail[1] + 0)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)
            elif tail_lag == (0, -2):
                rope_tail = (rope_tail[0] + 0, rope_tail[1] - 1)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)

            elif tail_lag == (1, 2):
                rope_tail = (rope_tail[0] + 1, rope_tail[1] + 1)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)
            elif tail_lag == (2, 1):
                rope_tail = (rope_tail[0] + 1, rope_tail[1] + 1)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)
            elif tail_lag == (2, -1):
                rope_tail = (rope_tail[0] + 1, rope_tail[1] - 1)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)
            elif tail_lag == (1, -2):
                rope_tail = (rope_tail[0] + 1, rope_tail[1] - 1)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)
            elif tail_lag == (-1, -2):
                rope_tail = (rope_tail[0] - 1, rope_tail[1] - 1)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)
            elif tail_lag == (-2, -1):
                rope_tail = (rope_tail[0] - 1, rope_tail[1] - 1)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)
            elif tail_lag == (-2, 1):
                rope_tail = (rope_tail[0] - 1, rope_tail[1] + 1)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)
            elif tail_lag == (-1, 2):
                rope_tail = (rope_tail[0] - 1, rope_tail[1] + 1)
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)
            else:
                rope_tail = rope_tail
                print(f"rope_tail: {rope_tail}")
                tail_coordinates.append(rope_tail)

        print("==========")

    print(len(set(tail_coordinates)))


if __name__ == "__main__":
    main()
