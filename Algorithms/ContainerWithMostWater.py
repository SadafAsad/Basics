from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        for x in range(len(height), 0, -1):
            for y_index in range(len(height)-x):
                storage = x*min(height[y_index], height[y_index+x])
                if storage>=ans:
                    ans = storage
        return ans