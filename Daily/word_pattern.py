"""
Problem Link: 

Task: 
    
Note:

Example 1:
    
Constraints:
    
"""

from typing import List

# TODO: Fill out problem description and add comments

class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:
            if len(pattern) != len(s.split()): return False
            pattern_dict: dict = {}
            words: list = s.split()
            used: set = set()
            for letter in pattern:
                word = words.pop(0)
                if letter not in pattern_dict and word not in used:
                    pattern_dict[letter] = word
                    used.add(word)
                elif word in used and letter not in pattern_dict:
                    return False
                elif pattern_dict[letter] != word:
                    return False
            return True