"""
Task
    Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Constraints
    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def bfs(self, root: Optional[TreeNode]) -> List[List[int]] :
        # list to store tree nodes val by lvl 
        levels = []
        # queue to store nodes on current lvl
        queue = []
        # append the root since there will only be one node on the root lvl
        levels.append([root.val])
        queue.append(root)
        while queue:
            # stores the # of nodes in queue (which reflects the # of nodes on the current lvl since were doing BFS)           
            num_of_nodes_on_lvl: int = len(queue)
            # while the number of nodes on the current lvl is not visited     
            while (num_of_nodes_on_lvl):
                # get the nodes out in FIFO
                node: Optional[TreeNode] = queue.pop(0)
                # Queue the left and right nodes into the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                # decremnent to reach end loop 
                num_of_nodes_on_lvl -= 1
            # only add to tree if queue has nodes
            if queue:
                # add nodes of the current level tree
                levels.append([node.val for node in queue])
        return levels

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # no point of tranversing an empty tree
        if not root:
            return []
        # if the root node is also a leaf, 
        if not root.left and not root.right:
            # return just the root node.  
            return [[root.val]]

        return self.bfs(root=root)
        

                