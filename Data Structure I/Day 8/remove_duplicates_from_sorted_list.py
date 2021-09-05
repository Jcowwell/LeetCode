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

        if head.next is None:
            return head

        # head pointer to return
        root : Optional[ListNode] = head
        # to sotre previous node in loop
        prev_node: Optional[ListNode] = None
        # set of numbers to check dups against
        numbers: set = set()

        while head:
            # if the head val is not in out number set
            if head.val not in numbers:
                # add it to our set
                numbers.add(head.val)
                # set the current node as a previous node for the next iteration 
                prev_node = head
            # our current node's value has poped up already
            else:
                # set the previous node to the current node's next node 
                prev_node.next = head.next
            # move to next node in list
            head = head.next
        return root


list1 = [1,1,2,3,3]
l1 = LinkedList(head=ListNode(list1[0]))
for value in list1[1:]:
    l1.append(ListNode(value))

Solution().reverseList(head = l1.head)