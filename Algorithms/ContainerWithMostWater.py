################### Question #########################

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

################### SOLUTION 1 ########################

# This is the first thing that you wrote.
# Eventhough it doesn't work for large arrays and you get Time Exceed, I'm gonna leave it here, because of the idea behind it.
# This is right but you need to optimize it. When you are lessning the area (x), you can choose which side to lessen it from.
# The smaller height won't give you any other better result that the larger height.
# So leave that behind and don't work on it --> Solution 1.1

# Time Complexity = O(n^2)
# Space Complexity = O(1)

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        for x in range(len(height), 0, -1):
            for y_index in range(len(height)-x):
                ans = max(x*min(height[y_index], height[y_index+x]), ans)
        return ans
    
################### SOLUTION 1.1 ########################

# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]: left += 1
            else: right -= 1

        return maxArea