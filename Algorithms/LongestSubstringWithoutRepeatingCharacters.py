################### Question ########################

# Given a string s, find the length of the longest substring without repeating characters.

################### SOLUTION 1 ######################

# The initial solution that I thought of was creating ALL the possible substrings
# removing those with repeated characters in them
# and then looking for the longest one. This one would have been of O(n^2) and it's a brute force solution.
# However, the next solution will only traverse the string once.
# It will create a new string and will traverse trhough the original string to add the characters.
# But before adding, will look if the new character to be added is already in there.
# If yes, then it will truncate from the beginning till after the index that was found and create a new string.
# through this process we will, keep record of the longest substring that was seen.
# Time Complexity = O(n)
# Space Complexity = O(n)

class Solution:
    def lengthOfLongestSubstring(self, str):
        str_tmp = ""
        max_len = 0
        max_len_tmp = 0
        for ch in str:
            if ch not in str_tmp:
                str_tmp+=ch
                max_len_tmp+=1
            else:
                found_in = str_tmp.index(ch)
                # the new substring
                str_tmp = str_tmp[found_in+1:]
                str_tmp+=ch
                # update the max length accordingly
                if max_len<max_len_tmp:
                    max_len = max_len_tmp
                max_len_tmp = len(str_tmp)
        if max_len<max_len_tmp:
            max_len = max_len_tmp
        return max_len