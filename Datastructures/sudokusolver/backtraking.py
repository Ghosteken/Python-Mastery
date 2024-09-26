def is_safe_sudoku(board, row, col, num, N):
    for i in range(N):
        if board[row][i] == num or board[i][col] == num:
            return False

    box_start_row, box_start_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + box_start_row][j + box_start_col] == num:
                return False

    return True

def solve_sudoku(board, N):
    empty_cell = find_empty_cell(board, N)
    if not empty_cell:
        return True

    row, col = empty_cell
    for num in range(1, N + 1):
        if is_safe_sudoku(board, row, col, num, N):
            board[row][col] = num
            if solve_sudoku(board, N):
                return True
            board[row][col] = 0

    return False

def find_empty_cell(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return i, j
    return None


sudoku_board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

if solve_sudoku(sudoku_board, 9):
    for row in sudoku_board:
        print(row)
else:
    print("No solution exists.")
