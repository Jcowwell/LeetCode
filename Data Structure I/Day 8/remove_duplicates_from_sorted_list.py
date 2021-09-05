"""
Task
    Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Constraints
    The number of nodes in the list is in the range [0, 300].
    -100 <= Node.val <= 100
    The list is guaranteed to be sorted in ascending order
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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head

        # head pointer to return
        root : Optional[ListNode] = head

        while root:
            # while the current node has a next node & the current node and next node values are eq
            while root.next and root.val == root.next.val:
                # set the current node's next node to the next node's next
                root.next = root.next.next
            # iterate through the node list
            root = root.next
        return head


list1 = [1,1,2,3,3]
l1 = LinkedList(head=ListNode(list1[0]))
for value in list1[1:]:
    l1.append(ListNode(value))

Solution().reverseList(head = l1.head)