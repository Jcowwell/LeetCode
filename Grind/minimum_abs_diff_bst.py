"""
Problem Link: 

Task: 
    
Note:

Example 1:
    
Constraints:
    
"""

from typing import Optional

# TODO: Fill out problem description and add comments

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        nums: list = []
        result: int = 10**5 + 1
        def dfs(root:TreeNode):
            if not root:
                return
            dfs(root.left)
            nums.append(root.val)
            dfs(root.right)
        dfs(root)
        for index in range(1,len(nums)):
            result = min(result, nums[index]-nums[index-1])
        return result