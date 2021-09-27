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

    # FIXME: - Add Annotations
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
        rows, columns = len(matrix), len(matrix[0])
        flat_lst: list[int] = []
        for row in range(rows):
            for col in range(columns):
                flat_lst.append(matrix[row][col])

        return self.__binary_search(lst = flat_lst, value=target)
    
Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3)
Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13)
        
