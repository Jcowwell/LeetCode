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
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        string_length = len(s)
        p_length = len(p)
        
        if len(s) < len(p):
            return []
        indices: list = []

        p_hash = sum(map(hash,p))
        current_hash = sum(map(hash,s[:p_length]))
        
        for index in range(string_length-p_length):
            if current_hash == p_hash:
                indices.append(index)
            current_hash = current_hash - hash(s[index]) + hash(s[index+p_length])
            
        if current_hash == p_hash: indices.append(string_length-p_length)
        
        return indices