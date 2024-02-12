#!/usr/bin/pyhton3

"""
   N-QUEENS ALGORITHIM:
    Example:
       0010
       1000 
       0001
       0100
"""


import sys

class NQueensSolver:
    """ Solves n queen problem """
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]

    def is_safe(self, row, col):
        # Check if there is a queen in the same column
        for i in range(row):
            if self.board[i][col] == 1:
                return False
        
        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False
        
        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.n)):
            if self.board[i][j] == 1:
                return False
        
        return True

    def solve_nqueens_util(self, row):
        if row == self.n:
            # Print the solution
            for i in range(self.n):
                for j in range(self.n):
                    print(self.board[i][j], end=' ')
                print()
            print()
            return True
        
        res = False
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                res = self.solve_nqueens_util(row + 1) or res
                self.board[row][col] = 0  # Backtrack
            
        return res

    def solve_nqueens(self):
        if not isinstance(self.n, int):
            print("N must be a number")
            sys.exit(1)
        
        if self.n < 4:
            print("N must be at least 4")
            sys.exit(1)
        
        if not self.solve_nqueens_util(0):
            print("No solution exists")
            sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        solver = NQueensSolver(N)
        solver.solve_nqueens()
    except ValueError:
        print("N must be a number")
        sys.exit(1)
