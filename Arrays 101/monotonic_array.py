"""
Task
    An array is monotonic if it is either monotone increasing or monotone decreasing.
    An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
    Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Constraints:
    1 <= nums.length <= 105
    -105 <= nums[i] <= 105
"""

from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if len(nums) ==  1:
            return True
        
        # indicator flags
        inc_flag = dec_flag = eq_flag = False

        
        # monotone increasing
        if nums[0] - nums[1] < 0:
            inc_flag = True
        # monotone decreasing
        elif nums[0] - nums[1] > 0:
            dec_flag = True
        # monotone same
        elif nums[0] == nums[1]: 
            eq_flag = True

        # iterate through list and stop if list is not monotonic
        for index, element in enumerate(nums[:-1]):
            if inc_flag:
                # if the list starts decreasing ... houston we have a problem
                if element > nums[index+1]:
                    return False
            elif dec_flag:
                # if the list starts increasing ... houston we have a problem
                if element < nums[index+1]:
                    return False
            elif eq_flag:
                """ 
                if the list does not contain all the same elements
                lets see if the list should be increasing or decreasing and then the loop will take care of the rest
                """
                if element != nums[index+1]:
                    # montone increasing
                    if element - nums[index+1] < 0:
                        inc_flag = True
                    # monotone decreasing
                    elif element - nums[index+1] > 0:
                        dec_flag = True
                    eq_flag = False

        # return if list was not stopped
        return True
            
Solution().isMonotonic(nums = [1,2,2,3])
Solution().isMonotonic(nums = [6,5,4,4])
Solution().isMonotonic(nums = [1,3,2])
Solution().isMonotonic(nums = [5,3,2,4,1])
Solution().isMonotonic(nums = [1,1,0])
Solution().isMonotonic(nums = [2,2,2,1,4,5])

