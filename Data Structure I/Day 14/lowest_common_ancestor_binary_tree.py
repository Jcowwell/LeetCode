"""
Task
    Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
    According to the definition of LCA on Wikipedia: 
    “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has 
    both p and q as descendants (where we allow a node to be a descendant of itself).”

Constraints
    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the BST.
"""

from typing import Optional

# FIXME: Annotate and utilize the fact the the lowest common ancestor will be a vlaue inbetween p and q
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    def compare_ancestors(self, longer_ancestor: dict, shorter_ancestor: dict) -> Optional[TreeNode]:
        shorter_ancestor_list = list(shorter_ancestor.items())
        while shorter_ancestor_list:
            s_element = shorter_ancestor_list.pop()
            if s_element[0] in longer_ancestor:
                return s_element[1]
        return None

    def search_ancestors(self, node: Optional[TreeNode], target: set, ancestors: dict) -> dict:
        if not node:
            return {}

        ancestors[node.val] = node

        if node.val == target:
            return ancestors
        
        if node.val > target:
            return self.search_ancestors(node.left, target=target, ancestors=ancestors)
        elif node.val < target:
            return self.search_ancestors(node.right, target=target, ancestors=ancestors)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return TreeNode()
        p_ancestors: dict = self.search_ancestors(node=root, target=p.val, ancestors= {})
        q_ancestors: dict = self.search_ancestors(node=root, target=q.val, ancestors= {})

        p_size, q_size  = len(p_ancestors), len(q_ancestors)

        common_ancestor: Optional[TreeNode] = None

        if p_size == q_size or p_size > q_size:
            common_ancestor = self.compare_ancestors(longer_ancestor=p_ancestors, shorter_ancestor=q_ancestors)
        elif p_size < q_size:
            common_ancestor = self.compare_ancestors(longer_ancestor=q_ancestors, shorter_ancestor=p_ancestors)
        
        return common_ancestor
    
        


root = TreeNode(val=5,
    left=TreeNode(val=3, left= TreeNode(val=2, left=TreeNode(1)), right=TreeNode(val=4)),
    right=TreeNode(val=6)
)

Solution().lowestCommonAncestor(root=root, p=root.left.left.left, q=root.left)