"""
Task
    Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.
    Each letter in magazine can only be used once in ransomNote.

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # dict to hold occurences that a char appears in string
        char_occurences: dict = {}

        # for characters in ransomNote string
        for char in ransomNote:
            # if character is in the dict then
            if char in char_occurences:
                # lets increment 
                char_occurences[char] += 1
            # not in occurences so 
            else:
                # lets "inititlize" it
                char_occurences[char] = 1
        
        # for characters in magazine  
        for char in magazine:
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

Solution().canConstruct(ransomNote = "a", magazine = "b")
Solution().canConstruct(ransomNote = "aa", magazine = "ab")
Solution().canConstruct(ransomNote = "aa", magazine = "aab")