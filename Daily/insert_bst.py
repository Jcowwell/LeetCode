"""
Problem Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/

Task: 
    
Note:

Example 1:
    
Constraints:
    
"""

# TODO: Fill out problem description and add comments

from typing import  Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # BST Rules:
            # The left subtree of a node contains only nodes with keys lesser than the node's key.
            # The right subtree of a node contains only nodes with keys greater than the node's key.
            # The left and right subtree each must also be a binary search tree.

        if not root:
            return TreeNode(val=val) # since there's no node to insert we should a node of the target value

        curr_node: TreeNode = root
        prev_node: Optional[TreeNode] = None 
        insert_node: TreeNode = TreeNode(val=val)

        while curr_node:
            prev_node: TreeNode = curr_node
            if curr_node.val > val:
                curr_node = curr_node.left
            elif curr_node.val < val:
                curr_node = curr_node.right

        if prev_node.val > val:
            prev_node.left = insert_node
        else:
            prev_node.right = insert_node
        
        return root