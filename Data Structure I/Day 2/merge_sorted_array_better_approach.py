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
        
        # three pointer varibles (2 for comparing, one for inserting) for in-place inserting
        pointer_1, pointer_2, index = m-1, n-1, m+n-1

        # while our iteration over the second list is not done
        while pointer_2 >= 0:
            # if we havent reach the end of our first list and the last element in the first list is bigger than the last element in the second list
            if pointer_1 >= 0 and nums1[pointer_1] > nums2[pointer_2]:
                # assign the biggest element in our first list to the back
                nums1[index] = nums1[pointer_1]
                # decrement our second list pointer
                pointer_1 -= 1
            # we've either finished iterating through our first list or the last element in the second lsit is bigger than the last element in our first list
            else:
                nums1[index] = nums2[pointer_2]
                # decrement out first list pointer
                pointer_2 -= 1
            # decrement our index access variable
            index -= 1

        
Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)