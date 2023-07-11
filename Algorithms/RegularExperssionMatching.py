################### Question #########################

# Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
# '.' Matches any single character.​​​​
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).

# Constraints:
# 1 <= s.length <= 20
# 1 <= p.length <= 20
# s contains only lowercase English letters.
# p contains only lowercase English letters, '.', and '*'.
# It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

################### SOLUTION 1 ########################

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_index = 0
        p_index = 0
        while p_index<len(p) and s_index<len(s):
            # any single character could be matched with .
            if p[p_index]==".":
                p_index+=1
                s_index+=1
            elif p[p_index]=="*":
                if p[p_index-1]==".":
                    if p_index==len(p)-1: return True
                    else: p_index+=1
                elif s[s_index]==p[p_index-1]:
                    while s[s_index]==p[p_index-1]:
                        s_index+=1
                        if s_index==len(s): break
                    p_index+=1
                else: return False
            else:
                if s[s_index]==p[p_index]:
                    s_index+=1
                    p_index+=1
                elif p_index<len(p)-2:
                    if p[p_index+1]=="*": p_index+=2
                else: return False
        
        if p_index==len(p) and s_index==len(s): return True
        elif s_index==len(s) and p[p_index-1]=="*":
            s_rtol = len(s)-1
            p_rtol = len(p)-1
            while s_rtol>0 and p_rtol>=p_index:
                if s[s_rtol]==p[p_rtol]:
                    s_rtol-=1
                    p_rtol-=1
                elif p[p_rtol]=="*" and p_rtol-1>0:
                    p_rtol-=1
                    if s[s_rtol]==p[p_rtol]:
                        while s[s_rtol]==p[p_rtol]:
                            s_rtol-=1
                            p_rtol-=1
                    else: p_rtol-=1
                else: return False
            return True
        else: return False