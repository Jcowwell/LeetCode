"""
Task
    In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.
    You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
    The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
    If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    -1000 <= mat[i][j] <= 1000
    1 <= r, c <= 300

"""

from typing import List


class Solution:

    def chunks(self, lst: list, chunk: int):
        for i in range(0, len(lst), chunk):
            yield lst[i:i + chunk] 

    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows, columns = len(mat), len(mat[0])
        reshaped_mat: List[List[int]] = []
        # a reshapable matrix should have the same product
        if rows * columns == r * c:
            if rows == r and columns == c:
                return mat
            else:
                # flatten out our list for chunkification
                column = []
                # iterate through rows
                for row in range(rows):
                    # iterate through columns
                    for col in range(columns):
                        # append to 1-d list
                        column.append(mat[row][col])
                # chunkification
                for chunk in self.chunks(column, c):
                    reshaped_mat.append(chunk)
            return reshaped_mat
        return mat

Solution().matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4)
Solution().matrixReshape(mat = [[1,2],[3,4]], r = 2, c = 4)
Solution().matrixReshape(mat = [[1,2,3,4]], r = 1, c = 4)
Solution().matrixReshape(mat = [[375,18,-195,568,-767,-14,37,434,80,286,-805,654,88,-922,-189,500,782,651,-623],[301,463,357,487,555,821,-978,-630,649,-56,-618,407,405,-870,-629,-582,678,366,-453],[815,-927,-547,-990,-357,947,202,240,-476,130,710,-748,-192,154,-768,21,210,861,266],[-85,-126,400,-425,730,40,242,321,-774,-182,94,-230,-697,281,-526,80,-413,529,131],[-856,882,-168,287,513,-817,346,418,703,-985,-882,-70,-407,876,-779,495,-712,-979,-586],[-659,915,-37,618,795,-754,187,427,-654,-258,918,525,175,-265,-520,-993,446,926,846],[105,628,-494,211,747,670,-717,71,-860,476,-474,-168,566,8,106,-407,0,-524,-150],[-431,-652,495,553,-902,237,521,916,-542,-167,-242,676,667,674,-196,471,441,-453,743],[330,278,-899,237,-795,145,-41,591,-924,-526,-651,785,995,-358,-893,-664,-902,769,458]], r = 19, c = 9)