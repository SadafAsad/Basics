################### SOLUTION 1 ########################

# In this solution we are simply merging the two arrays and at the end returning the median
# The merging step is done by traversing both arrays and appending the min number each step
# Time Complexity = O(m+n)
# Space Complexity = O(m+n)

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_array = []
        nums1_index = 0
        nums2_index = 0
        for i in range(len(nums1)+len(nums2)):
            if nums1_index<len(nums1) and nums2_index<len(nums2):
                if nums1[nums1_index]<=nums2[nums2_index]:
                    sorted_array.append(nums1[nums1_index])
                    nums1_index+=1
                else:
                    sorted_array.append(nums2[nums2_index])
                    nums2_index+=1
            elif nums1_index<len(nums1):
                sorted_array.append(nums1[nums1_index])
                nums1_index+=1
            else:
                sorted_array.append(nums2[nums2_index])
                nums2_index+=1
        
        if len(sorted_array)%2==1:
            return sorted_array[len(sorted_array)//2]
        return (sorted_array[len(sorted_array)//2]+sorted_array[len(sorted_array)//2-1])/2