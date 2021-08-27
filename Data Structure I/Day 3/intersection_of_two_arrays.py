"""
Task
    Given two integer arrays nums1 and nums2, 
    return an array of their intersection. 
    Each element in the result must appear as many times as it shows in both arrays and 
    you may return the result in any order.

    Constraints:
        1 <= nums1.length, nums2.length <= 1000
        0 <= nums1[i], nums2[i] <= 1000
 

Follow up:
    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""

from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersects: List[int] = []
        nums1_Counter, nums2_Counter = Counter(nums1), Counter(nums2)
        for num, occurence in nums1_Counter.items():
            num2_occurence = nums2_Counter[num]
            if num2_occurence != 0:
                if num2_occurence >= occurence:
                    intersects.extend([num] * occurence)
                else:
                    intersects.extend([num] * num2_occurence)
        return intersects


Solution().intersect(nums1 = [1,2,2,1], nums2 = [2,2])
Solution().intersect(nums1 = [4,9,5], nums2 = [9,4,9,8,4])