################### Question ########################

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

################### SOLUTION 1 ########################

# In this solution we'll start from the first entry and look for it's compliment in indexes after itself.
# Time Complexity = O(n^2)
# Space Complexity = O(n) 

class Solution:
    def twoSum(self, nums, target):
        num_index = 0
        while num_index<len(nums):
            compliment = target-nums[num_index]
            compliment_index = num_index+1
            while compliment_index<len(nums):
                if nums[compliment_index]==compliment:
                    return [num_index,compliment_index]
                compliment_index+=1
            num_index+=1
        return []

################### SOLUTION 2 ########################
    
# In this solution we'll sort the array with Merge Sort algorithm
# Merge Sort Time Complexity = O(nlogn)
# Merge Sort Space Complexity = O(n)
# Now we will have two moving indexing (sliding windows), one on the start of the array and the other on the last slot
# We will check sum of those two numbers in the moving indexes
# IF greater than target:
# then it means there is no other number in the array that could be summed with the last index to give us target
# so we will move the last index one slot to the left (-1)
# ELSE IF less than our target:
# then it means there is no other number that could be summed with the first index and give us target
# so we will move the first index one slot to the right (+1)
# we'll keep doing this until the two indexes are equal or pass each other
# Time Complexity = O(nlong)
# Space Complexity = O(n)
# DO NOT FORGET THAT WE NEED TO RETURN THE ORIGINAL INDEXES
# We need to look for those two numbers in the original nums array and return their index
# this will be of O(n) complexity which is ignorable(!)

class Solution:
    def twoSum(self, nums, target):
        # Sort nums
        sorted_nums = []
        for num in nums:
            sorted_nums.append(num)
        self.mergeSort(sorted_nums)

        # Looking for the numbers
        min_index = 0
        max_index = len(sorted_nums)-1
        found = False
        while min_index<max_index:
            sum_of_moving_indexes_nums = sorted_nums[min_index]+sorted_nums[max_index]
            if sum_of_moving_indexes_nums>target:
                max_index-=1
            elif sum_of_moving_indexes_nums<target:
                min_index+=1
            else:
                found = True
                break
        
        # Returning the original indexes
        if found:
            first_index_to_return = -1
            moving_on_nums = 0
            while moving_on_nums<len(nums):
                if nums[moving_on_nums]==sorted_nums[min_index] or nums[moving_on_nums]==sorted_nums[max_index]:
                    if first_index_to_return==-1:
                        first_index_to_return = moving_on_nums
                    else:
                        return [first_index_to_return,moving_on_nums]
                moving_on_nums+=1
        else:
            return []
        
    # CREDITS: https://www.educative.io/answers/merge-sort-in-python        
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            # Recursive call on each half
            self.mergeSort(left)
            self.mergeSort(right)

            # Two iterators for traversing the two halves
            i = 0
            j = 0
            
            # Iterator for the main list
            k = 0
            
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    # The value from the left half has been used
                    nums[k] = left[i]
                    # Move the iterator forward
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                # Move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k]=right[j]
                j += 1
                k += 1

################### SOLUTION 3 ########################

# This is done using hash table
# For each of the numbers in the array we will add its compliment to the hash table
# And every time we come up to the next number we will first check the compliment hash table
# if it was in the table it means that this is a compliment to a number already seen in the array 
# if not we will add it's compliment to the hash table to see if we will see it's compliment later
# Time Complexity = O(n)
# Space Complexity = O()

from typing import List

class Solution:
    def twoSumV3(self, nums: List[int], target: int) -> List[int]:
        # Hash Table -> {key=compliment, value=index}
        compliments = {}
        for i in range(len(nums)):
            # Has this number been a compliment?
            first_index = compliments.get(nums[i], -1)
            if first_index != -1:
                return [first_index, i]
            
            # Has not been a compliment
            compliment = target-nums[i]
            compliments[compliment] = i
        return []