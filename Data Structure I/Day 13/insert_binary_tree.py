"""
Task
    You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
    Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
    Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Constraints
    The number of nodes in the tree will be in the range [0, 104].
    -108 <= Node.val <= 108
    All the values Node.val are unique.
    -108 <= val <= 108
    It's guaranteed that val does not exist in the original BST.
"""

from typing import Optional

# FIXME: ANNOTATE

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        head = root
        tail = head

        while head:
            if head.val < val: 
                tail = head
                head = head.right   
            elif head.val > val: 
                tail = head
                head = head.left

        if tail.val < val:
            tail.right = TreeNode(val)
        elif tail.val > val:
            tail.left = TreeNode(val)

        return root

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

Solution().insertIntoBST(root=root, val=5)
        