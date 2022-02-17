"""
Problem Link: 

Task: 
    
Note:

Example 1:
    
Constraints:
    
"""

from typing import List

# TODO: Fill out problem description and add comments

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        width: int = len(arr)

        if width < 3: return False
        if width == 3: return (arr[0] < arr[1] > arr[2])

        increasing: bool = arr[0] < arr[1]
        decreasing: bool = False

        prev: int = arr[0]

        for index in range(1,width):
            if prev == arr[index]:
                return False
            if increasing:
                if prev > arr[index]:
                    increasing = False
                    decreasing = True
                    prev = arr[index]
                    continue
            elif decreasing:
                if prev < arr[index]:
                    return False
            else: 
                return False
            prev = arr[index]
            
        return decreasing