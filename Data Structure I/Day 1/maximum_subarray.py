"""
Task
    Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
    A subarray is a contiguous part of an array.

Constraints:
    1 <= nums.length <= 3 * 104
    -105 <= nums[i] <= 105

My Notes:
    In computer science, the maximum sum subarray problem is the task of finding a contiguous subarray 
    with the largest sum, within a given one-dimensional array A[1...n] of numbers.

    Some properties of this problem are:
        If the array contains all non-negative numbers, then the problem is trivial; a maximum subarray is the entire array.
        If the array contains all non-positive numbers, then a solution is any subarray of size 1 containing the maximal value of the array (or the empty subarray, if it is permitted).
        Several different sub-arrays may have the same maximum sum.

"""

from typing import List

class Solution:
    # taken from: https://en.wikipedia.org/wiki/Maximum_subarray_problem
    def __kadane(self, nums: List[int]) -> int:
        # # inf initilization disallows empty subarrays
        best_sum: float = float('-inf')
        # to keep track of sum as we loop
        current_sum: int = 0
        for num in nums:
            # by using max we reset current sum to either the current number or current_sum + num if current_sum + current number > current number
            current_sum = max(num, current_sum + num)
            # store whatever the best current_sum was duirng the loop.
            # having an -inf value ensures at least 1 value from the list is used
            best_sum = max(best_sum, current_sum)
        return best_sum

    # taken from: https://en.wikipedia.org/wiki/Maximum_subarray_problem
    def __kadane_w_indicies(self, nums: List[int]) -> tuple[int,int,int]:
        # inf initilization disallows empty subarrays
        best_sum: float = float('-inf')
        current_sum: int = 0
        best_start = best_end = 0  # or: None
        for current_end, x in enumerate(nums):
            # if out current sum is eq to or below 0
            if current_sum <= 0:
                # Start a new sequence at the current element
                current_start = current_end
                # Add to our current sum
                current_sum = x
            else:
                # Extend the existing sequence with the current element
                current_sum += x
            # when the current_sum is bigger than what was our best sum
            if current_sum > best_sum:
                # set the new bigger sum to best sum
                best_sum = current_sum
                # the best starting index would be where the new bigger value started from
                # this will only increment if the previous current_sum drops below 0 and then the current current sum is bigger than the stored best value
                best_start = current_start
                # best ending index would be where we stop looping.
                # this increments as the current_sum gets bigger
                best_end = current_end + 1  # the +1 is to make 'best_end' exclusive

        return best_sum, best_start, best_end

    def max_subarray(self, nums: List[int]) -> int:
        return self.__kadane(nums=nums)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))


