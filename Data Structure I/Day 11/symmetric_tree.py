"""
Task
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Constraints
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""

from typing import Optional, List

# FIXME: ANNOTATE

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def __postorderTraversal(self, node: TreeNode, values: List[int])-> List[int]:
        if node:
            self.__postorderTraversal(node=node.left, values=values)
            self.__postorderTraversal(node=node.right, values=values)
            values.append(node.val)
        else:
            values.append(None)
        return values
    def __reversepostorderTraversal(self, node: TreeNode, values: List[int])-> List[int]:
        if node:
            self.__reversepostorderTraversal(node=node.right,  values=values)
            self.__reversepostorderTraversal(node=node.left, values=values)
            values.append(node.val)
        else:
            values.append(None)
        return values

    def parallelTranversal(self, root: Optional[TreeNode]) -> bool :

        left_tranversal = self.__postorderTraversal(node=root.left, values = [])
        right_tranversal = self.__reversepostorderTraversal(node=root.right, values = [])

        if len(left_tranversal) != len(right_tranversal):
            return False
        for index in range(len(left_tranversal)):
            if left_tranversal[index] != right_tranversal[index]:
                return False
            
        return True

        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # no point of tranversing an empty tree
        if not root:
            return False
        # if the root node is also a leaf, 
        if not root.left and not root.right:
            # return just the root node.  
            return True
        if (root.left and not root.right) or (not root.left and root.right):
            return False

        return self.parallelTranversal(root=root)
        