"""
Problem Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

Task: 
    
Note:

Example 1:
    
Constraints:
    
"""

# TODO: Fill out problem description

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1]) # sort points by the x-end 
        ans = arrows = 0  # ans is the min number of arrows and arrows keeps track of where the current arrow is placed for comparisons 
        for [start,end] in points: 
            if ans == 0 or start > arrows: # the first boolean expression is for placing the first arrow at the end of the first point
                ans, arrows = ans + 1, end # when an point's starting position is greater than the current arrow's position then we need another arrow to hit this one. 
        return ans