#!/usr/bin/python3
"""
Nqueens problem
"""

import sys

def backtrack(r, n, cols, pos, neg, board):
    """
    Uses backtracking to find all possible solutions for the N-queens problem.

    Parameters:
    - r: Current row being evaluated.
    - n: Size of the board (n x n).
    - cols: Set of columns with queens.
    - pos: Set of positive diagonals with queens.
    - neg: Set of negative diagonals with queens.
    - board: 2D list representing the board. 1 indicates a queen, 0 indicates an empty square.

    Returns:
    None. All solutions are printed directly from this function.
    """
    if r == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Initiates the backtrack function for the N-queens problem.

    Parameters:
    - n: Size of the board (n x n).

    Returns:
    None. All solutions are printed directly from the backtracking function.
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
