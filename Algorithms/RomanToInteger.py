################### Question #########################

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as IV. 
# Because the one is before the five we subtract it making four. 
# The same principle applies to the number nine, which is written as IX. 
# There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

################### SOLUTION 1 ########################

# Time Complexity = O(n)
# Space Complexity = O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        ans = 0
        # Checking the last two elements
        while i<len(s)-1:
            # 1
            if s[i]=="I":
                # 4
                if s[i+1]=="V":
                    ans+=4
                    i+=2
                # 9
                elif s[i+1]=="X":
                    ans+=9
                    i+=2
                else:
                    ans+=1
                    i+=1
            # 5
            elif s[i]=="V":
                ans+=5
                i+=1
            # 10
            elif s[i]=="X":
                # 40
                if s[i+1]=="L":
                    ans+=40
                    i+=2
                # 90
                elif s[i+1]=="C":
                    ans+=90
                    i+=2
                else:
                    ans+=10
                    i+=1
            # 50
            elif s[i]=="L":
                ans+=50
                i+=1
            # 100
            elif s[i]=="C":
                # 400
                if s[i+1]=="D":
                    ans+=400
                    i+=2
                # 900
                elif s[i+1]=="M":
                    ans+=900
                    i+=2
                else:
                    ans+=100
                    i+=1
            # 500
            elif s[i]=="D":
                ans+=500
                i+=1
            # s[i]=="M" / 1000
            else:
                ans+=1000
                i+=1

        # Checking the last element if any left
        if i==len(s)-1:
            if s[i]=="I": return ans+1
            elif s[i]=="V": return ans+5
            elif s[i]=="X": return ans+10
            elif s[i]=="L": return ans+50
            elif s[i]=="C": return ans+100
            elif s[i]=="D": return ans+500
            else: return ans+1000
        
        return ans