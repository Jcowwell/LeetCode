"""
Task
    Given a binary tree, find its minimum depth.
    The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Constraints
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # FIXME: REWORD LOGIC TO WORK WITH MINDEPTH
    def dfs(self, root: Optional[TreeNode]):
        # return once we reached a leaf
        if not root:
            return 0
        # recursivly calls left side until reaches leaf
        # adds recursive sum to left_depth variable
        left_depth = self.dfs(root.left)
        # recursivly calls right side until reaches leaf
        # adds recursive sum to right_depth variable
        right_depth = self.dfs(root.right)
        # returns 1 + the whichever side was bigger
        return 1 + max(left_depth, right_depth)

        
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # no point of tranversing an empty tree
        if not root:
            return 0
        # if the root node is also a leaf, 
        if not root.left and not root.right:
            # return just the root node.  
            return 1

        return self.dfs(root=root)
        

                