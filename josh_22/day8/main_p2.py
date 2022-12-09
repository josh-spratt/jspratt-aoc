from typing import AnyStr, List


def read_input_file(file_path: AnyStr) -> List[AnyStr]:
    """Reads input file as a list"""
    print(f"Reading input file '{file_path}' to a list...")
    with open(file_path, "r") as f:
        return [line.rstrip() for line in f.readlines()]


def convert_input_to_matrix(input_data: List) -> List[List]:
    output_matrix = []
    for line in input_data:
        output_matrix.append([char for char in line])
    return output_matrix


def main():
    input = read_input_file("josh_22/input_files/day8.txt")
    forest_matrix = convert_input_to_matrix(input)
    int_matrix = [list(map(int, x)) for x in forest_matrix]
    scenic_scores = []
    for i in range(0, len(int_matrix)):
        for j in range(0, len(int_matrix[0])):
            tree_of_interest = int_matrix[i][j]
            print("|-------------------------------|")
            print(f"tree of interest\t{tree_of_interest}")
            northern_trees = []
            eastern_trees = []
            southern_trees = []
            western_trees = []

            # North
            for k in range(i - 1, -1, -1):
                check_tree = int_matrix[k][j]
                if check_tree < tree_of_interest:
                    northern_trees.append(check_tree)
                elif check_tree == tree_of_interest or check_tree > tree_of_interest:
                    northern_trees.append(check_tree)
                    break

            # East
            for k in range(j + 1, len(int_matrix[0])):
                check_tree = int_matrix[i][k]
                if check_tree < tree_of_interest:
                    eastern_trees.append(check_tree)
                elif check_tree == tree_of_interest or check_tree > tree_of_interest:
                    eastern_trees.append(check_tree)
                    break

            # South
            for k in range(i + 1, len(int_matrix)):
                check_tree = int_matrix[k][j]
                if check_tree < tree_of_interest:
                    southern_trees.append(check_tree)
                elif check_tree == tree_of_interest or check_tree > tree_of_interest:
                    southern_trees.append(check_tree)
                    break

            # West
            for k in range(j - 1, -1, -1):
                check_tree = int_matrix[i][k]
                if check_tree < tree_of_interest:
                    western_trees.append(check_tree)
                elif check_tree == tree_of_interest or check_tree > tree_of_interest:
                    western_trees.append(check_tree)
                    break

            northern_trees.reverse()
            western_trees.reverse()

            print(f"north:\t{northern_trees}")
            print(f"east:\t{eastern_trees}")
            print(f"south:\t{southern_trees}")
            print(f"west:\t{western_trees}")

            scenic_scores.append(
                len(northern_trees)
                * len(eastern_trees)
                * len(southern_trees)
                * len(western_trees)
            )
    print(max(scenic_scores))


if __name__ == "__main__":
    main()
