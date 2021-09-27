"""
Task
    Given the root of a binary tree, determine if it is a valid binary search tree (BST).

    A valid BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Constraints
    The number of nodes in the tree is in the range [1, 104].
    -231 <= Node.val <= 231 - 1
"""

from typing import Optional
from sys import maxsize

# FIXME: ANNOTATE
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isBST(self, node: Optional[TreeNode], min: int, max: int ) -> bool: 
        
        if not node:
            return True
        if node.val <= min or node.val >= max:
            return False
        
        return self.isBST(node.left, min, node.val) and self.isBST(node.right, node.val, max)


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.isBST(root, -maxsize, maxsize)

root = TreeNode(val=32,
    left=TreeNode(val=26,
        left=TreeNode(val=19,left=None,right=TreeNode(27)),
        right=None
        )
    ,
    right=TreeNode(val=47,
        left=None,
        right=TreeNode(56)
        )
)

Solution().isValidBST(root=root)