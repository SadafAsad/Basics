################### Question ########################

# Given a string s, return the longest palindromic substring in s.

################### SOLUTION 1 ######################
# Credits to LeetCode
# This is a brute force solution and we are checking all the subsrtings to see if we find any palindromic ones.
# We'll start checking with the longest substrings so then as soon as one is found we can returned it.
# Using the function 'check', we'll give it start and end index of the substring to check for it being palindromic or not
# Time Complexity = O(n^3)
# Space Complexity = O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            return True
        
        # checking substrings with different length, starting from the longest ones, len(s)
        for length in range(len(s), 0, -1):
            # We are basically moving the start index based on the length of the substring
            # first time we are looking for len(s) length substrings which is only one so start will only be 0
            # second round we are looking for len(s)-1 lengths which means there will be two substrings with that length
            # [0:len(s)] and [1:len(s)+1] and so on
            for start in range(len(s) - length + 1):
                # As soon as the check function returns True the first time
                # That will be the longest palindromic substring
                # The rest found after that will be shorter
                if check(start, start + length):
                    return s[start:start + length]
        return ""