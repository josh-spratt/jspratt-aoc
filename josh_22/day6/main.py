from typing import AnyStr, List


def read_input_file(file_path: AnyStr) -> List[AnyStr]:
    """Reads input file as a list"""
    print(f"Reading input file '{file_path}' to a list...")
    with open(file_path, "r") as f:
        return [line.rstrip() for line in f.readlines()]


def main():
    raw_lines = read_input_file("josh_22/input_files/day6.txt")
    
    # Part 1
    start_of_packet = []
    for datastream_buffer in raw_lines:
        buffer_packet = []
        counter = 0
        for i in range(0, len(datastream_buffer) + 1):
            slice = set([*datastream_buffer[i:i+4]])
            if len(slice) == 4 and counter == 0:
                buffer_packet.append(i+4)
                counter += 1
        start_of_packet.append(buffer_packet)
    print(f"Part 1 characters needed to be processed before first start-of-packet marker: {start_of_packet[0][0]}")

    # Part 2
    start_of_packet = []
    for datastream_buffer in raw_lines:
        buffer_packet = []
        counter = 0
        for i in range(0, len(datastream_buffer) + 1):
            slice = set([*datastream_buffer[i:i+14]])
            if len(slice) == 14 and counter == 0:
                buffer_packet.append(i+14)
                counter += 1
        start_of_packet.append(buffer_packet)
    print(f"Part 2 characters needed to be processed before first start-of-packet marker: {start_of_packet[0][0]}")


if __name__ == "__main__":
    main()
