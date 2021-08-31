"""
Task
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row.

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104  
"""

from typing import List

class Solution:


    def __binary_2D_search(self, lst: List[List[int]], value: int) -> bool:
        # get dimensions of the matrix
        M = len(lst) 
        N = len(lst[0])
        start, end = 0, M - 1
        
        while start <= end:
            # get middle of parittion (first iteration will be , middle of matrix)
            mid = (start + (end-start) // 2)
            # assign row and column based on mid 
            row, col = (mid // N), (mid % N)
            if lst[row][col] > value: end = mid - 1
            elif lst[row][col] < value: start = mid + 1
            else: return True
        return False

    def __binary_search(self, lst:list, value: int) -> bool:
        low = 0
        high = len(lst)-1
        while low <= high: 
            mid = (low+high)//2
            if lst[mid] > value: high = mid-1
            elif lst[mid] < value: low = mid+1
            else: return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # rows, columns = len(matrix), len(matrix[0])
        # flat_lst: list[int] = []
        # for row in range(rows):
        #     for col in range(columns):
        #         flat_lst.append(matrix[row][col])

        # return self.__binary_search(lst = flat_lst, value=target)

        return self.__binary_2D_search(lst= matrix, value=target)
    
Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
        
