"""
Task
    Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Constraints
    The number of nodes in the list is in the range [0, 104].
    1 <= Node.val <= 50
    0 <= val <= 50
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head
        self.current = self.head
    def append(self, node: ListNode):
        self.current.next = node
        self.current = node  

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # no need to iterate through a non-existant list
        if not head:
            return head

        # if we only have 1 node in the list
        if not head.next:
            # if the head node is eq to target value, return None
            if head.val == val: return None
            # else it doesn't so return head
            else: return head

        # head pointer node
        root: Optional[ListNode] = head
        # node to keep track of previous node
        prev_node: Optional[ListNode] = None

        # while we iterate through the nodes
        while head:
            # if were at the beginning of the list
            if prev_node is None:
                # if the head node's value is eq to target value
                if head.val == val:
                    # reset the head node pointer 
                    root = head.next                
                else:
                    # set the prev_node to head to start
                    prev_node = head
            # we are not at the head of the list
            else:
                # current node eq target value
                if head.val == val:
                    # stitch previous node's next to the node after the currenr, leaving out our current node
                    prev_node.next = head.next
                    # set head to previous node
                    head = prev_node
                # node is not target value
                else:
                    # set the precious node to the current node for the next loop
                    prev_node = head
            # "increment" through the node list be setting out head node to the next one
            head = head.next
        
        return root
                


list = [7,7,7,7]
l1 = LinkedList(head=ListNode(list[0]))
for value in list[1:]:
    l1.append(ListNode(value))


Solution().removeElements(head = l1.head , val = 7)
