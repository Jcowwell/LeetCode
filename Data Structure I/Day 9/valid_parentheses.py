"""
Task
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.

Constraints
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        
        # pairs dictonary to lookup ending pair via opening
        pairs: dict = {'{': '}', '(': ')', '[' : ']' }
        # set to verify opening part of pairs
        opening: set = {'{', '(', '['}
        
        # we know the pair isn't valid if there's not an even # of chars
        if len(s) % 2 != 0:
            return False

        # opening list to be used as a stack
        openings: list = []

        for char in s:
            if char in opening:
                # add opening to out stack for pop lookup
                openings.append(char)
            else:
                # if there's no openings to match to then the list is a dud
                if not openings:
                    return False
                # use pair dict as a lookup to compare to our current closing char
                elif pairs[openings.pop()] != char:
                    return False
        # if openings isn;t empty then there wasn't enough closing chars
        return len(openings) == 0

        


Solution().isValid(s = "{[]}")
Solution().isValid(s = "()[]{}")
Solution().isValid(s = "(]")
Solution().isValid(s = "([)]")
Solution().isValid(s = "((")