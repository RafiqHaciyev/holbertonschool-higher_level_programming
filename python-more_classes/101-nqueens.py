#!/usr/bin/python3
"""
N-Queens challenge: Placing N non-attacking queens on an N×N board.
This script finds all possible solutions using a backtracking algorithm.
"""
import sys


def solve_n_queens(n):
    """
    Initializes the backtracking process and prints all solutions.
    """
    board = []
    backtrack(n, 0, board)


def is_safe(board, row, col):
    """
    Checks if a queen can be placed at board[row][col].
    Since we place queens row by row, we only check for column
    and diagonal conflicts with previously placed queens.
    """
    for r, c in board:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def backtrack(n, row, board):
    """
    Uses recursion to find all valid queen placements.
    """
    if row == n:
        print(board)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            backtrack(n, row + 1, board)
            board.pop()  # Remove the queen to explore other possibilities


if __name__ == "__main__":
    # Validate the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Validate if N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Validate the value of N
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_n_queens(n)
