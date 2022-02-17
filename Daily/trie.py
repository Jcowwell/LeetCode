"""
Problem Link: 

Task: 
    
Note:

Example 1:
    
Constraints:
    
"""

from typing import List, Optional

# TODO: Fill out problem description and add comments

class Trie:

    def __init__(self):
        self.trie: dict = dict()

    def insert(self, word: str) -> None:
        current_dict: dict = self.trie
        for letter in word:
            current_dict = current_dict.setdefault(letter,{})
        current_dict[None] = None
    
    def search(self, word: str) -> bool:
        current_dict:dict = self.trie
        stack = [(current_dict,0,'')]
        result = []

        while stack:
            current_dict, count, current_word = stack.pop()

            if count == len(word):
                if None in current_dict: result.append(current_word)
                continue
                
            current_character: str = word[count]
            if current_character == '.':
                for letter, next_dict in current_dict.items():
                    if letter == None: continue
                    stack.append((next_dict, count + 1, current_word + letter))
                continue
            
            if current_character in current_dict:
                next_dict = current_dict[current_character]
                stack.append((next_dict, count+1, current_word + current_character))

        return len(result) > 0

    def startsWith(self, prefix: str) -> bool:
        """"""
        current_dict:dict = self.trie
        stack = [(current_dict,0,'')]
        prefixes = []

        while stack:
            current_dict, count, current_word = stack.pop()

            if count == len(prefix):
                prefixes.append(current_word)
                continue
                
            current_character: str = prefix[count]
            
            if current_character in current_dict:
                next_dict = current_dict[current_character]
                stack.append((next_dict, count+1, current_word + current_character))

        return len(prefixes) > 0

# def call(object: object, method_name: str, word: str):
#     if hasattr(object, method_name) and callable(func:=getattr(object,method_name)):
#         return func(word)

# trie : Trie = Trie()
# instructions: list = ["insert", "search", "search", "startsWith", "insert", "search"]
# arguments: list  = [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# results: list = []
# for i in range(len(instructions)):
#     results.append(
#         call(
#             object=trie,
#             method_name=instructions[i],
#             word = arguments[i][0]
#         )
#     )
# print(results)