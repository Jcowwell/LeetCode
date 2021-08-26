"""
Task
    Given an integer array nums sorted in non-decreasing order, 
    return an array of the squares of each number sorted in non-decreasing order. 

Constraints
    1 <= nums.length <= 104
    -104 <= nums[i] <= 104
    nums is sorted in non-decreasing order.
"""

from typing import List

class Solution:


    # O(n) when mirrored sorted list. 
    def stage_sort(self, nums: List[int]) -> List[int]:
        lst = [] * len(nums)
        # index to start at left of list
        left_index: int = 0
        #  index tp start at right of list
        right_index: int = len(nums) -1
        # until the left and right index are eq or pass eachother
        while left_index <= right_index:
            # if the left value is greater than the right
            if nums[left_index] > nums[right_index]:
                # add to return list
                lst.append(nums[left_index])
                # increment left
                left_index += 1
            # if the right value is greater than the left
            else:
                # add to return list
                lst.append(nums[right_index])
                # decrement right
                right_index -= 1
        # return a reverse splice of our list
        return lst[::-1]


    def sortedSquares(self, nums: List[int]) -> List[int]:
        self.stage_sort(nums=[num ** 2 for num in nums])
        
print(Solution().sortedSquares([x * x for x in range(-10,11)]))