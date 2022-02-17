"""
Problem Link: 

Task: 
    
Note:

Example 1:
    
Constraints:
    
"""

# TODO: Fill out problem description and add comments

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length : int = len(flowerbed)
            
        if length == 1:
            if (not(flowerbed[0]) and n == 1) or (flowerbed[0] and n == 0):
                return True
        
        for flower in range(0,len(flowerbed)):
            if n == 0:
                break
            if flower == 0:
                flip = 1 if not (flowerbed[flower] or flowerbed[flower+1]) else 0
                if flip:
                    flowerbed[flower] = 1
                    n -= 1
            elif flower == length -1:
                flip = 1 if not (flowerbed[flower] or flowerbed[flower-1]) else 0
                if flip:
                    flowerbed[flower] = 1
                    n -= 1
            else:
                flip = 1 if not (flowerbed[flower] or flowerbed[flower-1] or flowerbed[flower+1]) else 0
                if flip:
                    flowerbed[flower] = 1
                    n -= 1
        return n == 0 