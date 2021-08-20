"""
Problem Link: https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/

Task: 
    Given an array of integers nums, calculate the pivot index of this array.

    The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

    Return the leftmost pivot index. If no such index exists, return -1.

Example 1:
    Input: nums = [1,7,3,6,5,6]
    Output: 3
    Explanation:
    The pivot index is 3.
    Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
    Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
    Input: nums = [1,2,3]
    Output: -1
    Explanation:
    There is no index that satisfies the conditions in the problem statement.

Example 3:
    Input: nums = [2,1,-1]
    Output: 0
    Explanation:
    The pivot index is 0.
    Left sum = 0 (no elements to the left of index 0)
    Right sum = nums[1] + nums[2] = 1 + -1 = 0
 
Constraints:
    1 <= nums.length <= 104
    -1000 <= nums[i] <= 1000

Prefered Answer:

    Intuition and Algorithm

        We need to quickly compute the sum of values to the left and the right of every index.

        Let's say we knew S as the sum of the numbers, and we are at index i. If we knew the sum of numbers leftsum that are to the left of index i, then the other sum to the right of the index would just be S - nums[i] - leftsum.

        As such, we only need to know about leftsum to check whether an index is a pivot index in constant time. Let's do that: as we iterate through candidate indexes i, we will maintain the correct value of leftsum.

        class Solution(object):
            def pivotIndex(self, nums):
                S = sum(nums)
                leftsum = 0
                for i, x in enumerate(nums):
                    if leftsum == (S - leftsum - x):
                        return i
                    leftsum += x
                return -1
"""

from typing import List

def _pivot_index(nums: List[int], start_index: int, end_index: int) -> int:
        # choose left-most pivot
        pivot = 0
        # while the pivot is wihtin bounds
        while start_index <= pivot <= end_index:
            # if were at the first index then let's see if the right of the list is equal to 0
            if pivot == start_index and sum(nums[pivot+1:end_index+1]) == 0:
                return 0
            # if were at the last index then let's see if the right of the list is equal to 0
            elif pivot == end_index and sum(nums[start_index:end_index]) == 0:
                return end_index
            # if the sum of the two partitions is equal return pivot
            elif sum(nums[start_index:pivot]) == sum(nums[pivot+1:end_index+1]):
                return pivot
            else:
                # increase the pivot to the right by 1
                pivot += 1
        # no pivot index was found
        return -1

class Solution:

    def pivotIndex(self, nums: List[int]) -> int:

        nums_size: int = len(nums)

        # if the lists has only one element or has two elements and the second element is 0 return 0
        if nums_size == 1 or (nums_size == 2 and nums_size[1] == 0): 
            return 0

        return _pivot_index(nums=nums, start_index=0, end_index=nums_size-1)



    

