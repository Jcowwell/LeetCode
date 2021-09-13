"""
Task
    Implement a first in first out (FIFO) queue using only two stacks. 
    The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

    Implement the MyQueue class:

        void push(int x) Pushes element x to the back of the queue.
        int pop() Removes the element from the front of the queue and returns it.
        int peek() Returns the element at the front of the queue.
        boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

    You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head: list = [] 
        self.tail: list = [] 
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.head.append(x)
        self.tail.insert(0,self.head.pop())
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.tail.pop() if self.tail else None
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.tail[-1] if self.tail else None
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.tail

        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.peek()
obj.pop()
obj.empty()