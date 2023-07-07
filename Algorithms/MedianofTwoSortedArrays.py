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

from typing import List

# Be careful not to get confused. You are working with index! 
class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        na, nb = len(A), len(B)
        n = na + nb
        
        def solve(k, a_start, a_end, b_start, b_end):
            # If the segment of on array is empty, it means we have passed all
            # its element, just return the corresponding element in the other array.
            
            # AND to do so, you have to see how many elements you passed in the other one
            # to know which element to get from the remaining array
            # hence the - x_start
            if a_start > a_end: 
                return B[k - a_start]
            if b_start > b_end: 
                return A[k - b_start]

            # Get the middle indexes and middle values of A and B.
            a_mid_index, b_mid_index = (a_start + a_end) // 2, (b_start + b_end) // 2
            a_mid_value, b_mid_value = A[a_mid_index], B[b_mid_index]

            # If k is in the right half of A + B, remove the smaller left half.
            if a_mid_index + b_mid_index < k:
                # When removing the smaller left side, the k should also change
                # Cause removing elements after k effects k's place itself
               
                # Note here we are not changing k!
                # And that;s because we are not actually removing the elements after it
                # We are working with indexes and only changing those not the array itself.

                # To find out which left side is the smaller one
                # the mid is also being removed
                if a_mid_value > b_mid_value:
                    return solve(k, a_start, a_end, b_mid_index + 1, b_end)
                else:
                    return solve(k, a_mid_index + 1, a_end, b_start, b_end)
            # Otherwise, remove the larger right half. 
            else:
                # When removing the larger right side, the k doesn't have to change
                # Cause removing elements after k doesn't effect the k's place itself
                # However we were not changing k anyway, right? (reason in the above if statement)
                if a_mid_value > b_mid_value:
                    return solve(k, a_start, a_mid_index - 1, b_start, b_end)
                else:
                    return solve(k, a_start, a_end, b_start, b_mid_index - 1)
        
        # If n(A+B) is odd there is middle to the A+B hence the median
        if n % 2:
            # 5//2=2 this is the index of the median that we are looking for
            # Which means median is the 3rd element in the A+B
            return solve(n // 2, 0, na - 1, 0, nb - 1)
        # If n(A+B) is even there is no middle to the A+B hence two slots to calculate the median
        else:
            # 6//2=3 this is one of the slots and the other is 4
            # This means the 3rd and 4th elements of A+B
            return (solve(n // 2 - 1, 0, na - 1, 0, nb - 1) + solve(n // 2, 0, na - 1, 0, nb - 1)) / 2

################### SOLUTION 3 ######################

# Credits to LeetCode:
# Follows the same idea of solution 2. We are looking for an index in A and B to partition them in a way 
# that we can say we have found the smaller half of A and B that combined will be the smaller half of A+B.
# In this solution we are not going to find it on the A+B array but on the smaller array (let's assume A is the smaller one) -- in size!
# we'll start by diving it first from the middle (assume that the index in which the left half of A will definitely be in the left of A+B)
# And to find the index of B which indicates the same thing as mentioned, we'll assume it's (m+n+1)/2-partitionA.
# Reason being we want to say we have found indexes of A and B in which the'll make up the left half of A+B.
# Now we'll have to compare the edge slots to see if the indexes are right. If not we'll have to move partitionA 
# (this is were we are only searching on the smaller array and not A+B)
# Time Complexity = O(log(min(m,n)))
# Space Complexity = O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)


        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            # The first time it will be the middle index
            # Will change in next iterations based on the comparison of edges
            partitionA = (left + right) // 2
            # And this changes based on whatever is the A's partition
            partitionB = (m + n + 1) // 2 - partitionA

            # We'll get the edge elements here
            maxLeftA = float('-inf') if partitionA == 0 else nums1[partitionA - 1]
            minRightA = float('inf') if partitionA == m else nums1[partitionA]
            maxLeftB = float('-inf') if partitionB == 0 else nums2[partitionB - 1]
            minRightB = float('inf') if partitionB == n else nums2[partitionB]

            # this indicates we have found the right indexes!
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            # If maximum element of the left half of A is greater than the minimum element of the right half of B
            # Then it indicates that the maxLeftA is too large to be in the smaller half of A+B 
            # So we'll move it one to the left to push it in the right half of A being the greater half
            elif maxLeftA > minRightB:
                right = partitionA - 1
            # maximum element of left half of B is greater than the minimum element of the right half of A
            # it means that the minimum element of the right half of A is too small to be in the right half o A+B
            # So we'll move A's index one to the right to push that element to the left side being the smaller half
            else:
                left = partitionA + 1