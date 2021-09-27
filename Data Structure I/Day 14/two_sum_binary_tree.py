"""
Task
    Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

Constraints
    The number of nodes in the tree is in the range [1, 104].
    -104 <= Node.val <= 104
    root is guaranteed to be a valid binary search tree.
    -105 <= k <= 105
"""

from typing import Optional

# # FIXME: ANNOTATE & UTILIZE THE BINARY TREE TO FIND TO SUMS IN O(LOG(N)) TIME

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def preorderTranversal(self, node: Optional[TreeNode], values: set) -> None:
        if node:
            values.add(node.val)
            self.preorderTranversal(node=node.left, values=values)
            self.preorderTranversal(node=node.right, values=values)


    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False

        values: set = set()

        self.preorderTranversal(node=root, values=values)

        while values:
            value: int = values.pop()
            if (k- value) in values: return True
            
        return False


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