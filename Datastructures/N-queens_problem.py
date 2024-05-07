def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        solutions.append(list(board))
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row] = -1

def solve_n_queens(N):
    board = [-1] * N
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

# Example usage:
N = 4
queens_solutions = solve_n_queens(N)
for solution in queens_solutions:
    print(solution)
