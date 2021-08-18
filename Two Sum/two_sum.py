"""
Problem Link: https://leetcode.com/problems/two-sum/

Task: 

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # structure: difference found: subtractant
        differences = {}
        for index, element in enumerate(nums):
            # get # Needed to get Target
            difference = target - element
            # if the difference is eq to the element and there is more than one in the list let's return the first and second occurrence
            if difference == element and nums.count(difference) >= 2:
                # DN: Highly inefficient i know. 
                return [index, [i for i, n in enumerate(nums) if n == difference][1]]
            # check if element was already calculated beforehand
            if element in differences:
                # return if so
                return [differences[element], index]
            # Let's use dict to store the difference and index and then return if the element is an already sotred difference
            differences[target - element] = index
