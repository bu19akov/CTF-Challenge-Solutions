# Classic Sudoku

## Challenge Details 

- **CTF:** RingZer0
- **Category:** Coding Challenges
- **Points:** 7

## Provided Materials

- SSH credentials

## Solution

I don't know why, but when I was doing this task, I was able to connect with `SSH` in `Terminal`, but couldn't connect via `paramiko`, so I created the code, that will interpret sudoku field from `SSH` connection as it is, parse it and then solve. 

So I had 10 seconds to copy the sudoku field into my python code, execute it, copy the output (solved) string and paste it back in `Terminal`, but basically 10 seconds are enough for that.

Here is my code: 

```python 
from typing import List, Tuple, Optional

def is_valid(board: List[List[int]], row: int, col: int, num: int) -> bool:
    """
    Check if a number can be placed in the given row and column of the Sudoku board.
    """
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board: List[List[int]]) -> Optional[List[List[int]]]:
    """
    Solve the Sudoku puzzle using backtracking.
    """
    empty = find_empty(board)
    if not empty:
        return board  # Puzzle solved
    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return board
            board[row][col] = 0  # Reset the cell for backtracking

    return None  # Trigger backtracking

def find_empty(board: List[List[int]]) -> Optional[Tuple[int, int]]:
    """
    Find an empty cell in the Sudoku board (denoted by 0).
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return i, j  # row, col
    return None

def transform_sudoku_input(sudoku_string):
    """
    Transform a string representation of a Sudoku puzzle into a 2D list format.
    The input string has a specific format with | and + characters separating the numbers.
    Empty cells are represented by spaces.
    """
    sudoku_list = []
    for line in sudoku_string.split('\n'):
        if '|' in line:
            # Extract numbers and spaces, replace spaces with 0, and convert to integers
            row = [0 if x == '   ' else int(x) for x in line.split('|')[1:-1]]
            sudoku_list.append(row)
    return sudoku_list

# Sample input
sudoku_input = """
+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   | 6 |   | 5 |   |
+---+---+---+---+---+---+---+---+---+
| 3 | 5 | 9 | 4 | 8 |   |   |   |   |
+---+---+---+---+---+---+---+---+---+
| 8 |   |   |   |   | 1 | 9 |   |   |
+---+---+---+---+---+---+---+---+---+
| 1 |   |   | 2 |   |   |   |   | 6 |
+---+---+---+---+---+---+---+---+---+
|   |   | 4 |   |   | 5 | 1 |   | 3 |
+---+---+---+---+---+---+---+---+---+
|   |   | 8 |   |   |   |   | 4 |   |
+---+---+---+---+---+---+---+---+---+
|   | 8 |   |   |   |   | 3 |   |   |
+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   | 4 |   |   | 7 |
+---+---+---+---+---+---+---+---+---+
|   |   |   |   |   |   |   |   |   |
+---+---+---+---+---+---+---+---+---+
"""

# Transform the input
sudoku = transform_sudoku_input(sudoku_input)

# Solving the Sudoku
solved_sudoku = solve_sudoku(sudoku)
print(','.join(','.join(str(num) for num in row) for row in solved_sudoku))
```

## Final Flag

`FLAG-B6KF40aRVq6LS3Jy079IECWK1b`

*Created by [bu19akov](https://github.com/bu19akov)*