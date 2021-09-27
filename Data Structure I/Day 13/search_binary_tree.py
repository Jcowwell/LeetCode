"""
Task
    You are given the root of a binary search tree (BST) and an integer val.
    Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
    If such a node does not exist, return null.

Constraints
    The number of nodes in the tree is in the range [1, 5000].
    1 <= Node.val <= 107
    root is a binary search tree.
    1 <= val <= 107
"""

from typing import Optional

# FIXME: Annotate

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    # ineffcient preorder tranversal
    def __preorder_search(self, node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        leftSearch = rightSearch = None
        if node:
            if node.val == target:
                return node
            leftSearch = self.__preorder_search(node=node.left, target=target)
            rightSearch = self.__preorder_search(node=node.right, target=target)
        return leftSearch if rightSearch is None else rightSearch

    # efficient binary search
    def __binary_search(self, node: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        while node:
            if node.val < target: node = node.right
            elif node.val > target: node = node.left
            elif node.val == target: return node
        return None
    
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        return self.__binary_search(node=root, target=val)

root = TreeNode(val=4,
    left=TreeNode(val=2,
        left=TreeNode(val=1,
            left=None,
            right=None
        ),
        right=TreeNode(val=3,
            left=None,
            right=None
        ),
    ),
    right=TreeNode(val=7,
        left=None,
        right=None
    )
)

Solution().searchBST(root=root, val=2)
        