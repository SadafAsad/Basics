################### Question #########################

# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

################### SOLUTION 1 ########################

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        for x in range(len(height), 0, -1):
            for y_index in range(len(height)-x):
                container = x*min(height[y_index], height[y_index+x])
                if container>=ans:
                    ans = container
        return ans