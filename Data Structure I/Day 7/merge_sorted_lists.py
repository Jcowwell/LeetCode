"""
Task
    Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Constraints
    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both l1 and l2 are sorted in non-decreasing order.
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

    def mergeTwoLists(self, l1: list, l2: list) -> list:
        l1_pointer: int = 0
        l2_pointer: int = 0
        l3: list = []
        l3_length = len(l1) + len(l2)
        
        while l3_length > 0:
            if l1[l1_pointer] <= l2[l2_pointer]:
                l3.append(l1[l1_pointer])
                l1_pointer += 1 if l1_pointer < len(l1) - 1 else 0
                l3_length -= 1
            elif l1[l1_pointer] > l2[l2_pointer]: 
                l3.append(l2[l2_pointer])
                l2_pointer += 1 if l2_pointer < len(l2) - 1 else 0
                l3_length -= 1
        return l3

    def list_length(self, node: ListNode)-> int:
        count = 0
        while node:
            count +=1
            node=node.next
        return count

    def mergeTwoLinkedLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # No reason to iterate if one or both of our list is empty
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        # root node with initial dummy node
        root: Optional[ListNode] = ListNode()
        # tail node to point at the end of root node. will be udsed to append nodes at the end of root
        tail: Optional[ListNode] = root

        # while either list is not fully iterated through
        while l1 and l2:
            # if l1 value is smaller or equal to l2's
            if l1.val <= l2.val:
                # attach current l1 node to tail
                tail.next = l1
                # move to next node
                l1 = l1.next
            else: # if l2's value is smaller than l1's
                # attach current l2 node to tail
                tail.next = l2
                # move to next node
                l2 = l2.next
            # move the tail to the next node for insertion
            tail = tail.next
        
        # append last bits of node content in case of left over nodes in either list
        tail.next = l1 if l1 else l2

        return root.next


list1 = [5]
l1 = LinkedList(head=ListNode(list1[0]))
for value in list1[1:]:
    l1.append(ListNode(value))
list2 = [1,2,4]
l2 = LinkedList(head=ListNode(list2[0]))
for value in list2[1:]:
    l2.append(ListNode(value))

Solution().mergeTwoLists(l1 = [1,2,4], l2 = [1,3,4])
Solution().mergeTwoLinkedLists(l1 = l1.head, l2 = l2.head)