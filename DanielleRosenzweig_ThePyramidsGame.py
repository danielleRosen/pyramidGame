import random


def initialize_matrix():
    mat = [[0 for w in range(9)] for h in range(5)]  # create a matrix of size 5x9
    colors = ["blue", "yellow", "pink"]
    row = 0
    col = 4
    count = 0  # count how many slots on the right and the left of a given slot to set
    # set values to create a pyramid
    while row < 5 and count < 5:  # count cannot be bigger than 4 since the matrix has 9 columns
        mat[row][col] = random.choice(colors)
        for i in range(count):
            mat[row][col - (i + 1)] = random.choice(colors)
            mat[row][col + (i + 1)] = random.choice(colors)
        count += 1
        row += 1
    return mat


def check_second_condition(row, col, mat):
    is_satisfied = True
    if row > 0 and mat[row - 1][col] == "pink":
        is_satisfied = False
        return [is_satisfied, row - 1, col]
    if row < 4 and mat[row + 1][col] == "pink":
        is_satisfied = False
        return [is_satisfied, row + 1, col]
    if col < 8 and mat[row][col + 1] == "pink":
        is_satisfied = False
        return [is_satisfied, row, col + 1]
    if col > 0 and mat[row][col - 1] == "pink":
        is_satisfied = False
        return [is_satisfied, row, col - 1]
    return [is_satisfied, 0, 0]


def game():
    mat = initialize_matrix()
    colors = ["blue", "yellow", "pink"]
    all_conditions_satisfied = False
    while not all_conditions_satisfied:
        first_condition = True
        second_condition = True
        third_condition = True
        for row in range(5):
            yellow_sum = 0  # number of yellow slots in a row
            for col in range(9):
                if mat[row][col] == "blue":
                    if row == 4 or row + col == 4 or col - row == 4:  # first condition
                        first_condition = False
                        mat[row][col] = random.choice(colors)
                    else:
                        ans = check_second_condition(row, col, mat)  # answer for checking the second condition
                        if ans[0] is False:
                            second_condition = False
                            mat[ans[1]][ans[2]] = random.choice(colors)
                if row > 1 and mat[row][col] == "yellow":
                    yellow_sum += 1
            if yellow_sum > 4:
                third_condition = False
                for j in range(9):  # set new values for the entire row
                    mat[row][j] = random.choice(colors)
        all_conditions_satisfied = first_condition and second_condition and third_condition
    return mat


matrix = game()
for x in range(5):
    for y in range(9):
        if len(str(matrix[x][y])) == 6:
            print(matrix[x][y], '\t', end="")
        elif len(str(matrix[x][y])) == 4:
            print(matrix[x][y], '\t', end="")
        else:
            print(matrix[x][y], '\t\t', end="")
    print()
