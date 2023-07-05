################### Question ########################

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

################### SOLUTION 1 ######################

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
    
################### SOLUTION 2 ######################

# Credits to LeetCode: (-- in my own words tho ;) --)
# When you hear talking about finding something in sorted arrays, one things that should always pop in your head is binary search.
# In this questions we are looking for the median in two sorted arrays. (after the two has been merged together)
# Let's see what we can get if we compare their medians:
# If A's median is smaller than B's median, then we can conclude that the left side of A would've been completely to the left side of
# their merged array and B's right side would've been completely to the right side of their merged array. 
# (left and right with respect to the median to be found)
# So we can say number of(A left) elements would have been for sure in the left side of A+B 
# and number of(B right) elements would have been for sure in the right side of A+B
# Now let's see when we are talking about median what that actually means:
# where should we look for the median of A+B? in the middle right? which means n(A+B)/2
# (yeah, it differs when the number of elements is odd or even, but let's think about the concept for now)
# so let's say the median index (middle index) of our target (our median) is k
# This means we are looking for the k+1th element in the A+B (+1 is because k is index)
# WELL HELLO! we can know at least how many elements will be to the left side and right side of A+B by comparing their medians!
# That can help us to decide that k+1th element could possibly be to the left or right side!
# If k+1 is greater than half of the A+B elements then we can stop looking for it in the left side of A!
# Cause that side (the smaller side) will be for sure in the left side of A+B array and we know k+1th is not there
# And when it's smaller or equal to the half of the A+B elemenets then we can stop looking in the right side of B!
# Cause that side (the larger side) will be for sure in the right side of A+B array and we know k+1th is not there
# Time Complexity = O(logm+logn) = O(logmn)
# Space Complexity = O(logmn) <- only because of recursion otherwise we are allocating more than constant number of space


