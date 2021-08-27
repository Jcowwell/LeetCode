"""
Task
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
    representing the number of elements in nums1 and nums2 respectively.
    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
    To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
    and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109

"""

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index: int = 0
        while nums2:
            # if the pointer index is in no mands land 
            if index in range(m,m+n):
                # let's just assign the value from the second list to theno amnds land 0's position
                nums1[index] = nums2.pop(0)
                # increment index for next iteration
                index+=1
            # if the first element in the second list is greater than the current pointed element
            elif (nums2[0] > nums1[index]):
                # incremement index
                index += 1
            else:
                # pop out the first element in the second list into the second lists
                nums1.insert(index,nums2.pop(0))
                # pop out the 0 at the end of our first list
                nums1.pop()
                # increment our m to decrease our no mans land range
                m += 1
        
Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)