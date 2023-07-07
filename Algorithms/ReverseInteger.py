################### Question ########################

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

################### SOLUTION 1 ######################

class Solution:
    def reverse(self, x: int) -> int:
        positive = True
        if x<0:
            positive = False
            x*=-1
        ans = 0
        while x!=0:
            ans = ans*10+x%10
            x = x//10
        if positive and ans<2**31:
            return ans  
        elif ~positive and ans<2**31+1:
            return ans*-1
        return 0