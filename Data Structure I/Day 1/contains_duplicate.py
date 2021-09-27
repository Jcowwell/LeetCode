"""
Task
    Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

    Constraints:
        1 <= nums.length <= 105
        -109 <= nums[i] <= 109

"""
from typing import List

# FIXME: ANNOTATE

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_list_length: int = len(nums)
        nums_set_length: int = len(set(nums))
        if nums_list_length != nums_set_length:
            return True
        return False