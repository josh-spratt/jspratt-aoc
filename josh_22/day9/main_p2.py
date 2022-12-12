from typing import AnyStr, List
import json


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


def move_head(x_value, y_value, rope_head):
    rope_head = (
        rope_head[0] + x_value,
        rope_head[1] + y_value,
    )
    return rope_head


def move_tail(head, tail):
    tail_lag = (head[0] - tail[0], head[1] - tail[1])
    if tail_lag == (2, 0):
        tail = (tail[0] + 1, tail[1] + 0)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (0, 2):
        tail = (tail[0] + 0, tail[1] + 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (-2, 0):
        tail = (tail[0] - 1, tail[1] + 0)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (0, -2):
        tail = (tail[0] + 0, tail[1] - 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (1, 2):
        tail = (tail[0] + 1, tail[1] + 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (2, 1):
        tail = (tail[0] + 1, tail[1] + 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (2, -1):
        tail = (tail[0] + 1, tail[1] - 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (1, -2):
        tail = (tail[0] + 1, tail[1] - 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (-1, -2):
        tail = (tail[0] - 1, tail[1] - 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (-2, -1):
        tail = (tail[0] - 1, tail[1] - 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (-2, 1):
        tail = (tail[0] - 1, tail[1] + 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (-1, 2):
        tail = (tail[0] - 1, tail[1] + 1)
        print(f"tail: {tail}")
        return tail

    elif tail_lag == (2, 2):
        tail = (tail[0] + 1, tail[1] + 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (-2, -2):
        tail = (tail[0] - 1, tail[1] - 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (-2, 2):
        tail = (tail[0] - 1, tail[1] + 1)
        print(f"tail: {tail}")
        return tail
    elif tail_lag == (2, -2):
        tail = (tail[0] + 1, tail[1] - 1)
        print(f"tail: {tail}")
        return tail
    else:
        return tail


def main():
    raw_input = read_input_file(file_path="josh_22/input_files/day9.txt")
    rope = [(0, 0) for _ in range(10)]
    rope_head = rope[0]
    tail = rope[9]
    tail_coordinates = []
    tail_coordinates.append(tail)
    print("\n")
    print("==========")

    for line in raw_input:
        direction = line.split(" ")[0]
        print(f"The direction the rope will move:\t{direction}")
        value = int(line.split(" ")[1])
        print(f"The distance the rope will move:\t{value}")

        for j in range(1, value + 1):
            instruction = Instruction(direction=direction, value=j)
            x, y = instruction.convert_instruction_to_coord()
            rope[0] = move_head(x, y, rope[0])

            for i in range(1, len(rope)):
                rope[i] = move_tail(rope[i-1], rope[i])
                tail_coordinates.append(rope[9])

    print("==========")

    print(len(set(tail_coordinates)))


if __name__ == "__main__":
    main()
