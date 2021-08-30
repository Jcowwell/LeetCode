"""
Task
    Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        Each row must contain the digits 1-9 without repetition.
        Each column must contain the digits 1-9 without repetition.
        Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    
    Note:
        A Sudoku board (partially filled) could be valid but is not necessarily solvable.
        Only the filled cells need to be validated according to the mentioned rules.

    Constraints:
        board.length == 9
        board[i].length == 9
        board[i][j] is a digit or '.'.
"""

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns = len(board), len(board[0])
        
        # check columns
        for col in range(columns):
            seen = set()
            for row in range(rows):
                # check if digit
                if board[row][col].isdigit():
                    if board[row][col] in seen: return False
                    seen.add(board[row][col])

        # check rows
        for row in range(rows):
            seen = set()
            for element in board[row]:
                # check if digit
                if element.isdigit():
                    if element in seen: return False
                    seen.add(element)

        # check 3x3 multi-axis subset
        for x in range(0,9,3):
            for y in range(0,9,3):
                seen = set()
                for row in board[y:y+3]:
                    for element in row[x:x+3]:
                        # check if digit
                        if element.isdigit():
                            if element in seen: return False
                            seen.add(element)
        return True


Solution().isValidSudoku(board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

Solution().isValidSudoku(board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]])

Solution().isValidSudoku(board = 
[[".",".",".",".",".",".","5",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".",".",".",".",".",".","."]
,["9","3",".",".","2",".","4",".","."]
,[".",".","7",".",".",".","3",".","."]
,[".",".",".",".",".",".",".",".","."]
,[".",".",".","3","4",".",".",".","."]
,[".",".",".",".",".","3",".",".","."]
,[".",".",".",".",".","5","2",".","."]])
    