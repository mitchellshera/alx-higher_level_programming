#!/usr/bin/python3

import sys

def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nqueens(board, col):
    """Solve the N queens problem using backtracking."""
    # Base case: If all queens are placed
    if col >= N:
        print_solution(board)
        return True

    # Recursive case: Try placing a queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen at board[i][col]
            board[i][col] = 1

            # Recur for the remaining columns
            solve_nqueens(board, col + 1)

            # Backtrack: Remove the queen from board[i][col]
            board[i][col] = 0

    return False

def print_solution(board):
    """Print the solution in the required format."""
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

if __name__ == "__main__":
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from command line argument
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check the value of N
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty N x N chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N queens problem
    solve_nqueens(board, 0)
