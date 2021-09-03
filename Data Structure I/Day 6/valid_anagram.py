"""
Task
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # anagrams must be equal in length in order to be anagrams
        if len(s) != len(t):
            return False
        # loop through any char since they're anaygrams
        for char in s:
            # the count of specific chars must be the same 
            if s.count(char) != t.count(char):
                # return if not
                return False
        # t is an anagram of s!
        return True

Solution().isAnagram(s = "anagram", t = "nagaram")
Solution().isAnagram(s = "rat", t = "car")
Solution().isAnagram(s = "ab", t = "a")