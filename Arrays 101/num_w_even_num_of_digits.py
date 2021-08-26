"""
Task
    Given an array nums of integers, 
    return how many of them contain an even number of digits.

Constraints:
    1 <= nums.length <= 500
    1 <= nums[i] <= 10^5
"""

from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count: int = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count+= 1
        return count


nums: List[int] =  [555,901,482,1771]
print(Solution().findNumbers(nums))