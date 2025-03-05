import random

# function to check if the current number is valid in the given position
def is_valid(board, row, col, num):
    # check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


# backtracking function to solve the sudoku puzzle
def solve_sudoku(board):
    # find the next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # try numbers 1-9
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0  # backtrack
                return False
    return True


# function to count all solutions using backtracking
def count_solutions(board):
    count = [0]

    def count_recursive(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            count_recursive(board)
                            board[row][col] = 0  # backtrack
                    return
        count[0] += 1

    count_recursive(board)
    return count[0]


# function to generate a valid sudoku board with 10-30 pre-filled cells
def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    filled_cells = random.randint(10, 30)
    #filled_cells = 20

    # try filling random positions with valid numbers
    while filled_cells > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)

        if board[row][col] == 0 and is_valid(board, row, col, num):
            board[row][col] = num
            filled_cells -= 1

    return board


# display the sudoku board
def print_board(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else '.' for x in row))


# main function to generate a board, solve it, and count solutions
def main():
    board = generate_sudoku()

    print("initial sudoku board:")
    print_board(board)

    # solve the sudoku puzzle
    if solve_sudoku(board):
        print("\nsolved sudoku board:")
        print_board(board)
    else:
        print("\nno solution exists.")

    # count the number of valid solutions
    solution_count = count_solutions(board)
    print(f"\ntotal valid solutions: {solution_count}")


if __name__ == "__main__":
    main()
