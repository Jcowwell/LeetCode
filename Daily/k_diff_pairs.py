"""
Problem Link: https://leetcode.com/problems/k-diff-pairs-in-an-array/

Task: 
    
Note:

Example 1:
    
Constraints:
    
"""
# TODO: Fill out problem description and add comments

from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        occurances: dict = {}

        for num in nums:
            if num in occurances:
                occurances[num] += 1
            else:
                occurances[num] = 1
        
        count: int = 0
        for num, _ in occurances.items():
            if (k > 0 and num + k in occurances) or k == 0 and occurances[num] > 1:
                count += 1

        return count