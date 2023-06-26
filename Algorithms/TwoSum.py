# # In this solution we'll start from the first entry and look for it's compliment in indexes after itself.
# # Time Complexity = O(n^2)
# # Space Complexity = O(n) 
# class Solution:
#     def twoSumV1(self, nums, target):
#         num_index = 0
#         while num_index<len(nums):
#             compliment = target-nums[num_index]
#             compliment_index = num_index+1
#             while compliment_index<len(nums):
#                 if nums[compliment_index]==compliment:
#                     return [num_index,compliment_index]
#                 compliment_index+=1
#             num_index+=1
#         return []
    
# In this solution we'll sort the array with ? algorithm
# ? Time Complexity = O(n)
# ? Space Complexity = ?
# Now we will have two moving indexing (sliding windows), one on the start of the array and the other on the last slot
# We will check sum of those two numbers in the moving indexes
# IF greater than target:
# then it means there is no other number in the array that could be summed with the last index to give us target
# so we will move the last index one slot to the left (-1)
# ELSE IF less than our target:
# then it means there is no other number that could be summed with the first index and give us target
# so we will move the first index one slot to the right (+1)
# we'll keep doing this until the two indexes are equal or pass each other
# Time Complexity = O(n)
# Space Complexity = ?
# DO NOT FORGET THAT WE NEED TO RETURN THE ORIGINAL INDEXES
# We need to look for those two numbers in the original nums array and return their index
# this will be of O(n) complexity which is ignorable(!)

class Solution:
    def twoSumV2(self, nums, target):
        # SORT nums
        sorted_nums = nums

        # Looking for the numbers
        min_index = 0
        max_index = len(sorted_nums)
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
            second_index_to_return = -1
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
                
                    

            
