"""
Task
    Given the root of a binary tree, invert the tree, and return its root.

Constraints
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
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
    
    def swap_tranversal(self, node: Optional[TreeNode]) -> None:
        if node:
            temp: Optional[TreeNode] = node.left
            node.left = node.right
            node.right = temp
            self.swap_tranversal(node.left)
            self.swap_tranversal(node.right)
    
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        head: Optional[TreeNode] = root
        self.swap_tranversal(node=head)
        return root
            
        
        