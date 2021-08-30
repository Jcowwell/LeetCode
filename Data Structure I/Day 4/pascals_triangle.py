"""
Task
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Constraints:
    1 <= numRows <= 30
"""

from typing import List

class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        # first two rows of pascal's triangle cna be returned without calculation
        if numRows <= 0:
            return [[]]
        if numRows == 1:
           return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        # pascal's triangle initilized to the 3rd row
        pascal_triangle: List[List[int]] = [[1],[1,1],[1,2,1]]
        # start from 4 row
        for row in range(3,numRows):
            # row list to append at each row
            pascal_row = []
            # number of items in col is equal to row number
            for col in range(row+1):
                # if were not at the beginning or end of list
                if col != 0 and col != row:
                     # sum is eq to pr[i-1] + pr[i] where pr is the previous row
                    pascal_row.append(
                        pascal_triangle[row-1][col-1] + pascal_triangle[row-1][col]
                    )
                # were at the beginning/end of list
                else:
                    pascal_row.append(1)
            # add to pascal triangle
            pascal_triangle.append(pascal_row)
        return pascal_triangle
            



Solution().generate(numRows = 5)
