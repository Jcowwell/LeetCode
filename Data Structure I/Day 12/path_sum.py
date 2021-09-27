"""
Task
    Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
    A leaf is a node with no children.

Constraints
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""

from typing import Optional, List

# Definition for a binary tree node.
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __preorder_path_sum(self, node: Optional[TreeNode], sum: int, sums: set()):
        if not node:
            return sum

        sum += node.val
        
        if not node.left and not node.right:
            sums.add(sum)
            return sum
        else:
            self.__preorder_path_sum(node=node.left, sum=sum, sums=sums)
            self.__preorder_path_sum(node=node.right, sum=sum, sums=sums)
        
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        path_sums: set() = set()
        sum: int = 0
        self.__preorder_path_sum(node=root, sum=sum, sums=path_sums)
        
        return targetSum in path_sums
        
        