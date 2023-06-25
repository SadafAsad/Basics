class Solution:
    def twoSum(self, nums, target):
        num_index = 0
        while num_index<len(nums):
            compliment = target - nums[num_index]
            compliment_index = num_index+1
            while compliment_index<len(nums):
                if nums[compliment_index]==compliment:
                    return [num_index, compliment_index]
                compliment_index+=1
            num_index+=1
        return []