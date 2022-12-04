from collections import Counter


def main():
    # Read input file
    with open("josh_22/input_files/day1.txt") as f:
        list_of_cals = [x.rstrip() for x in f.readlines()]

    # Split out calorie list into elf-specific sublists
    elves = []
    counter = 0
    elves.append([])
    for line in list_of_cals:
        if line != "":
            elves[counter].append(line)
        else:
            counter += 1
            elves.append([])

    # Create a new list that contains the sum for each list
    new_list = sorted([sum([int(cal) for cal in elf]) for elf in elves])
    output_dict = {k: v for k, v in enumerate(new_list)}
    print(f"Maximum calorie sum for a single elf: {output_dict[max(output_dict)]}")
    top_3 = Counter(output_dict).most_common(3)
    print(f"The top 3 elves are: {top_3}")
    print(f"The sum of the top 3 elves: {sum([elf[1] for elf in top_3])}")


if __name__ == "__main__":
    main()
