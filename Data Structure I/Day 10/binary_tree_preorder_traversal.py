"""
Task 
    Given the root of a binary tree, return the preorder traversal of its nodes' values.

Constraints:

    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100
"""

from typing import Optional, List

from numpy import append

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # private worker function
    def __preorderTraversal(self, node: TreeNode, values: List[int]) -> List[int]:
        # while the current node is not a leaf (end of node tranversal) 
        if node:
            # append root node
            values.append(node.val)
            # then go through left nodes
            self.__preorderTraversal(node = node.left, values=values)
            # then go through right nodes
            self.__preorderTraversal(node = node.right, values=values)

    # public driver function
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # no point of tranversing an empty tree
        if not root:
            return []
        # if the root node is also a leaf, 
        if not root.left and not root.right:
            # return just the root node.  
            return [root.val]
        # list to store node values
        values: List[int] = []
        # run private worker function
        self.__preorderTraversal(node=root, values=values)
        
        return values

       
