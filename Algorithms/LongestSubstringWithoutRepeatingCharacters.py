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

################### SOLUTION 1 - Slightly Different ######################

# The next solution has the same logic as the last one.
# The only difference is that it's not using the built-in "index" function of python
# Instead, it's using another iterator on the substring to pop until the character is not in there anymore
# And will also use it o calculate the max length.

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         max_len = 0
#         char_lst = []
#         i=j=0
#         while i<len(s) and j<len(s):
#             if s[j] not in char_lst:
#                 char_lst.append(s[j])
#                 j+=1
#             else:
#                 max_len = max(max_len, j-i)
#                 char_lst.pop(0)
#                 i+=1
#         return max(max_len, len(char_lst))
