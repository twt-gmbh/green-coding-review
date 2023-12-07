# import tracemalloc
# tracemalloc.start()

from typing import List

# Q: Give me a memory optimized solution for this problem. Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).

# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #find the median of two sorted arrays
        #merge two sorted arrays
        #find the median of the merged array
        #return the median
        #O(n+m) time and O(n+m) space
        #O(log(n+m)) time and O(1) space is the requirement
        #binary search  O(log(n+m)) time and O(1) space
        #find the median of the merged array
        #return the median