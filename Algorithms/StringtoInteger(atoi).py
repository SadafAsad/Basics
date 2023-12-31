################### Question #########################

# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# The algorithm for myAtoi(string s) is as follows:
# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. 
# This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. 
# Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 
# Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.
# Note:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

################### SOLUTION 1 ########################

# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def myAtoi(self, s: str) -> int:
        start = 0
        # ignoring whitespace characters
        while start<len(s):
            if s[start]==" ":
                start+=1
            else:
                break
        
        # determining integer's sign
        if start<len(s):
            if s[start]=="-":
                sign = -1
                start+=1
            elif s[start]=="+":
                sign = 1
                start+=1
            elif ord(s[start])>=ord('0') and ord(s[start])<=ord('9'):
                sign = 1
            else:
                return 0
        else:
            return 0

        # retrieving the integer
        integer = 0
        while start<len(s) and ord(s[start])>=ord('0') and ord(s[start])<=ord('9'):
            integer = integer*10+ord(s[start])-48
            start+=1

        # checking in bound integer
        if sign==1:
            if integer<=2**31-1:
                return integer*sign
            return 2**31-1
        else:
            if integer<=2**31:
                return integer*sign
            return -(2**31)

