def main():
    # Read input file
    with open("josh_22/input_files/day2.txt") as f:
        data_list = [x.rstrip().split(" ") for x in f.readlines()]

    # A = Rock
    # B = Paper
    # C = Scissors
    # X = Rock 1
    # Y = Paper 2
    # Z = Scissors 3
    # L = 0, D = 3, W = 6
    points = []
    for match in data_list:
        points_counter = 0
        if match[1] == "X" and match[0] == "A":
            points_counter += 1
            points_counter += 3
            points.append(points_counter)
        elif match[1] == "X" and match[0] == "B":
            points_counter += 1
            points.append(points_counter)
        elif match[1] == "X" and match[0] == "C":
            points_counter += 1
            points_counter += 6
            points.append(points_counter)
        elif match[1] == "Y" and match[0] == "A":
            points_counter += 2
            points_counter += 6
            points.append(points_counter)
        elif match[1] == "Y" and match[0] == "B":
            points_counter += 2
            points_counter += 3
            points.append(points_counter)
        elif match[1] == "Y" and match[0] == "C":
            points_counter += 2
            points.append(points_counter)
        elif match[1] == "Z" and match[0] == "A":
            points_counter += 3
            points.append(points_counter)
        elif match[1] == "Z" and match[0] == "B":
            points_counter += 3
            points_counter += 6
            points.append(points_counter)
        elif match[1] == "Z" and match[0] == "C":
            points_counter += 3
            points_counter += 3
            points.append(points_counter)

    print(sum(points))

    # A = Rock
    # B = Paper
    # C = Scissors
    # X = Lose
    # Y = Draw
    # Z = Win
    # L = 0, D = 3, W = 6
    points = []
    for match in data_list:
        points_counter = 0
        if match[1] == "X" and match[0] == "A":
            # scissors loses to rock
            points_counter += 3
            points.append(points_counter)
        elif match[1] == "X" and match[0] == "B":
            # rock loses to paper
            points_counter += 1
            points.append(points_counter)
        elif match[1] == "X" and match[0] == "C":
            # paper loses to scissors
            points_counter += 2
            points.append(points_counter)
        elif match[1] == "Y" and match[0] == "A":
            # rock draws rock
            points_counter += 1
            points_counter += 3
            points.append(points_counter)
        elif match[1] == "Y" and match[0] == "B":
            # paper draws paper
            points_counter += 2
            points_counter += 3
            points.append(points_counter)
        elif match[1] == "Y" and match[0] == "C":
            # scissors draws scissors
            points_counter += 3
            points_counter += 3
            points.append(points_counter)
        elif match[1] == "Z" and match[0] == "A":
            # paper beats rock
            points_counter += 2
            points_counter += 6
            points.append(points_counter)
        elif match[1] == "Z" and match[0] == "B":
            # scissors beats paper
            points_counter += 3
            points_counter += 6
            points.append(points_counter)
        elif match[1] == "Z" and match[0] == "C":
            # rock beats scissors
            points_counter += 1
            points_counter += 6
            points.append(points_counter)

    print(sum(points))


if __name__ == "__main__":
    main()
