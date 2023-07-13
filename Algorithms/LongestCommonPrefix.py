################### Question #########################

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

################### SOLUTION 1 ########################

# The whole idea behind this solution is very simple:
# We're gonna check each character of each string in the array
# So we'll first get the min length of the existing strings in the array 
# Then we'll need two loops, one to iterate over the characters and the other to iterate over the array of strings
# Time Complexity = O(n^2)
# Space Complexity = O(1)

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        for str in strs:
            min_len = min(min_len, len(str))

        prefix = ""
        char_index = 0
        while char_index<min_len:
            for i in range(len(strs)):
                if strs[0][char_index]!=strs[i][char_index]:
                    return prefix
            prefix+=strs[0][char_index]
            char_index+=1
        
        return prefix
