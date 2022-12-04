from typing import List, AnyStr, Dict
import argparse
from pprint import pprint

# Global Variables
ALPHABET = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

NUMBERS = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
]


def read_input_file(file_path: str) -> List[AnyStr]:
    """Reads input file as a list"""
    print(f"Reading input file '{file_path}' to a list...")
    with open(file_path, "r") as f:
        return [line.rstrip() for line in f.readlines()]


def find_matching_item_types(rucksacks: List[AnyStr]) -> List:
    rucksacks_list = [[char for char in compartment] for compartment in rucksacks]
    item_types_list = []
    for rucksack in rucksacks_list:
        rucksack_split_point = len(rucksack) // 2
        compartment_a = rucksack[:rucksack_split_point]
        compartment_b = rucksack[rucksack_split_point:]
        item_types_list.extend(list(set(compartment_a).intersection(compartment_b)))
    return item_types_list


def find_matching_item_types_per_group_members(rucksacks: List[AnyStr]) -> List:
    rucksacks_list = [[char for char in compartment] for compartment in rucksacks]
    item_types_list = []
    groups_list = zip(*(iter(rucksacks_list),) * 3)
    for group in groups_list:
        member_one = group[0]
        member_two = group[1]
        member_three = group[2]
        item_types_list.extend(
            list(set(member_one).intersection(member_two).intersection(member_three))
        )
    return item_types_list


def build_priority_mapping_dict(letters: List, priorities: List) -> Dict:
    return dict(zip(letters, priorities))


def main():
    # Argparsing for input file path
    parser = argparse.ArgumentParser(description="Taking in the input file path.")
    parser.add_argument("file_path", type=str, help="Please enter the input file path.")
    args = parser.parse_args()

    rucksacks = read_input_file(file_path=args.file_path)

    # Part 1
    matching_item_types = find_matching_item_types(rucksacks=rucksacks)
    priority_map = build_priority_mapping_dict(letters=ALPHABET, priorities=NUMBERS)
    final_list = []
    for item_type in matching_item_types:
        if item_type in priority_map.keys():
            final_list.append(priority_map[item_type])
        elif item_type in [x.upper() for x in priority_map.keys()]:
            final_list.append(priority_map[item_type.lower()] + 26)
    print(f"Part 1 item type priority sum: {sum(final_list)}")

    # Part 2
    matching_item_types = find_matching_item_types_per_group_members(
        rucksacks=rucksacks
    )
    part2_final_list = []
    for item_type in matching_item_types:
        if item_type in priority_map.keys():
            part2_final_list.append(priority_map[item_type])
        elif item_type in [x.upper() for x in priority_map.keys()]:
            part2_final_list.append(priority_map[item_type.lower()] + 26)
    print(f"Part 2 item type priority sum: {sum(part2_final_list)}")


if __name__ == "__main__":
    main()
