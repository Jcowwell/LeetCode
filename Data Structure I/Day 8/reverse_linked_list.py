"""
Task
    Given the head of a singly linked list, reverse the list, and the return the reversed list

Constraints
    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000
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

        if head.next is None:
            return head

        # going to be the head of the reversal
        prev_node: Optional[ListNode] = None

        while head:
            # temporarily store the current node's next node
            temp = head.next
            # set the current node's next to the previous node [REVERSAL]
            head.next = prev_node
            # set previous node to current node for next iteration  
            prev_node = head
            # set the head to the current node's previous next node before reversal
            head = temp
        return prev_node


list1 = [x for x in range(0,5001)]
l1 = LinkedList(head=ListNode(list1[0]))
for value in list1[1:]:
    l1.append(ListNode(value))

Solution().reverseList(head = l1.head)