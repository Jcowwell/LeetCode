"""
Task
    Given a binary array nums, return the maximum number of consecutive 1's in the array.

Constraints:
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
"""


from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # keeps track of current count
        current_count: int = 0
        # to store best count
        best_count: int = 0
        # tweaked version of kadane's algorithm
        for num in nums:
            if num == 1:
                # increment if num eq 1
                current_count += 1
            else:
                # reset count
                current_count = 0
            # store the count if it is greater than past count
            best_count = max(best_count, current_count)
        return best_count

        

nums: List[int] = [1,1,0,1,1,1]
print(Solution().findMaxConsecutiveOnes(nums=nums))