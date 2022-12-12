from pprint import pprint
import re
from itertools import groupby
from typing import AnyStr, List
import math


class Monkey:
    def __init__(self, monkey_id=0, items=[], operation=None, test=None, send_true_to=0, send_false_to=0):
        self.monkey_id = monkey_id
        self.items = items
        self.operation = operation
        self.test = test
        self.send_true_to = send_true_to
        self.send_false_to = send_false_to


def read_input_file(file_path: AnyStr) -> List[AnyStr]:
    """Reads input file as a list"""
    print(f"Reading input file '{file_path}' to a list...")
    with open(file_path, "r") as f:
        return [x.strip() for x in f.read().split("\n")]


def monkey_investigation(monkey, item, divisor):
    if "* 3" in monkey.operation:
        worry_level = item * 3
    elif "* 11" in monkey.operation:
        worry_level = item * 11
    elif "+ 6" in monkey.operation:
        worry_level = item + 6
    elif "+ 4" in monkey.operation:
        worry_level = item + 4
    elif "+ 8" in monkey.operation:
        worry_level = item + 8 
    elif "+ 2" in monkey.operation:
        worry_level = item + 2
    elif "old * old" in monkey.operation:
        worry_level = item * item
    elif "+ 5" in monkey.operation:
        worry_level = item + 5
    elif "* 19" in monkey.operation:
        worry_level = item * 19  
    elif "* 19" in monkey.operation:
        worry_level = item * 19
    elif "+ 3" in monkey.operation:
        worry_level = item + 3                   

    worry_level %= divisor
    test_result = worry_level % monkey.test
    if test_result == 0:
        return True, worry_level
    else:
        return False, worry_level                              



def main():
    raw_monkeys = read_input_file(file_path="josh_22/input_files/day11.txt")
    split_monks = [list(g) for k, g in groupby(raw_monkeys, key=bool) if k]
    monkey_list = []
    for i in range(0, len(split_monks)):
        monkey_id = i
        monkey_items = [int(x) for x in re.findall("[0-9]+", split_monks[i][1])]
        monkey_operation = split_monks[i][2].split(": ")[1]
        monkey_test = int(re.findall("[0-9]+", split_monks[i][3])[0])
        if_true_send_to = int(re.findall("[0-9]+", split_monks[i][4])[0])
        if_false_send_to = int(re.findall("[0-9]+", split_monks[i][5])[0])
        monkey_list.append(
            Monkey(monkey_id, monkey_items, monkey_operation, monkey_test, if_true_send_to, if_false_send_to)
        )

    divisor = math.prod([x.test for x in monkey_list])
    inspection_counter = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0
    }
    x = 1
    while x <= 10000:
        for j in range(0, len(monkey_list)):
            while len(monkey_list[j].items) > 0:
                try:
                    evals_to, value = monkey_investigation(monkey_list[j], monkey_list[j].items[0], divisor)
                    inspection_counter[j] += 1
                    if evals_to:
                        monkey_list[monkey_list[j].send_true_to].items.append(value)
                    else:
                        monkey_list[monkey_list[j].send_false_to].items.append(value)
                    del monkey_list[j].items[0]
                except Exception as e:
                    print(e)    
        x += 1

    pprint(inspection_counter)


if __name__ == "__main__":
    main()
