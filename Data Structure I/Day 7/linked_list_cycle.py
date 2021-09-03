"""
Task
    Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
    Return true if there is a cycle in the linked list. Otherwise, return false.

Constraints
    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.
"""

# Definition for singly-linked list.
from multiprocessing.connection import Listener


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class LinkedList:
    def __init__(self, head: ListNode):
        self.head = head
        self.current = self.head
    def append(self, node: ListNode):
        self.current.next = node
        self.current = node  

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # We want to visit each node and mark it as visited
        # We can use a simple boolean value or a value outside of our Node.val range 
        # (ex. -10e6 or 10e6 would be fine)
        while head != None:
            
            # We will use the flag value of 10e6. If Node.val == 10e6 we've encountered a cycle
            # else change the node's value to 10e6 and move to the next node
            if head.val == 10e6:
                return True
            else:
                head.val = 10e6
                head = head.next
                
        # Breaking out of the while loop indicates we have no cycles
        # This would mean we encountered a node with Node.next = None
        return False

head = [3,2,0,-4]
linked_list = LinkedList(head=ListNode(head[0]))
for value in head[1:]:
    linked_list.append(ListNode(value))
Solution().hasCycle(head = linked_list.head)
linked_list = LinkedList(head=ListNode(head[0]))
for value in head[1:]:
    linked_list.append(ListNode(value))
linked_list.current.next = linked_list.head
Solution().hasCycle(head = linked_list.head)
