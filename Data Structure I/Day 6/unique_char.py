"""
Task
    Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Constraints:
    1 <= s.length <= 105
    s consists of only lowercase English letters.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:

        # blacklist for chars that repeat
        blacklist: set = set()
        #  dict to store letter and index position
        char_index: dict = {}
        # index variable to keep track of where a char index was through the second for in loop
        index: int = 0
        for index, char in enumerate(s):
            # skip if in blacklist
            if char in blacklist:
                continue
            # if not in blacklist yet we have just found it's second occurence, let's blacklist
            if char in char_index:
                blacklist.add(char)
                del char_index[char]
            else:
                # add to char index
                char_index[char] = index

        if char_index:
            # by taking advantage of Python 3.X perserve order of dict we cna return the first inserted value that remains
            return list(char_index.values())[0]

        # no unque chars were found. 
        return -1
        
        
        
Solution().firstUniqChar(s = "leetcode")
Solution().firstUniqChar(s = "loveleetcode")
Solution().firstUniqChar(s = "aabb")