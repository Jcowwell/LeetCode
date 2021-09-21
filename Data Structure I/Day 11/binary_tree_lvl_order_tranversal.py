"""
Task
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Constraints
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""

from typing import Optional, List
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def bfs(self, root: Optional[TreeNode]) -> List[List[int]] :
        tree = []
        queue = Queue()
        depth: dict = {}
        lvl: int = 0
        # visited: set = set()
        # visited.add(depth + root.val)
        tree.append([root.val])
        queue.put(root)

        while not queue.empty():
            # FIXME: use Queue size to help determine level
            node: Optional[TreeNode] = queue.get()
            nodes = []
            level: int = len(queue)
            if node.left:
                nodes.append(node.left.val)
                queue.put(node.left)
                print(f'level: {lvl}')
            if node.right:
                nodes.append(node.right.val)
                queue.put(node.right)
                print(f'level: {lvl}')
            if nodes:
                lvl += 1
                tree.append(nodes)
            
        return tree

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # no point of tranversing an empty tree
        if not root:
            return []
        # if the root node is also a leaf, 
        if not root.left and not root.right:
            # return just the root node.  
            return [[root.val]]

        return self.bfs(root=root)
        

                