def read_input_file(filepath: str) -> list:
    with open(filepath, "r") as f:
        return [int(x) for x in f.readlines()]


def main():
    input_list = read_input_file(filepath="aoc_2018/2018_input/day1_input.txt")
    resulting_frequency = 0
    for item in input_list:
        resulting_frequency += item
    print(f"The resulting frequency is: {resulting_frequency}")


if __name__ == "__main__":
    main()
