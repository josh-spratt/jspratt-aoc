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
    trees = []
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
            for k in range(0, i):
                check_tree = int_matrix[k][j]
                northern_trees.append(check_tree)

            # East
            for k in range(j + 1, len(int_matrix[0])):
                check_tree = int_matrix[i][k]
                eastern_trees.append(check_tree)

            # South
            for k in range(i + 1, len(int_matrix)):
                check_tree = int_matrix[k][j]
                southern_trees.append(check_tree)

            # West
            for k in range(0, j):
                check_tree = int_matrix[i][k]
                western_trees.append(check_tree)

            print(f"north:\t{set(northern_trees)}")
            print(f"east:\t{set(eastern_trees)}")
            print(f"south:\t{set(southern_trees)}")
            print(f"west:\t{set(western_trees)}")

            if (
                all(num < tree_of_interest for num in northern_trees)
                or all(num < tree_of_interest for num in eastern_trees)
                or all(num < tree_of_interest for num in southern_trees)
                or all(num < tree_of_interest for num in western_trees)
            ):
                trees.append(tree_of_interest)
        # print(trees)
        print(len(trees))


if __name__ == "__main__":
    main()
