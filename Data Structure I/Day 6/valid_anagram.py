"""
Task
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Constraints:
    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        # dict to hold occurences that a char appears in string
        char_occurences: dict = {}

        # for characters in ransomNote string
        for char in t:
            # if character is in the dict then
            if char in char_occurences:
                # lets increment 
                char_occurences[char] += 1
            # not in occurences so 
            else:
                # lets "inititlize" it
                char_occurences[char] = 1
        
        # for characters in magazine  
        for char in s:
            # if character exists 
            if char in char_occurences:
                # decrement occurence count
                char_occurences[char] -= 1
                # if the occurence count reaches 0 or below 
                if char_occurences[char] <= 0:
                    # remove from dict
                    del char_occurences[char]
            # if occurence dict is empty
            if not char_occurences:
                return True
        return False

Solution().isAnagram(s = "anagram", t = "nagaram")
Solution().isAnagram(s = "rat", t = "car")
Solution().isAnagram(s = "ab", t = "a")