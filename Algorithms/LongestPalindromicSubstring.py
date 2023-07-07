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

################### SOLUTION 2 ######################

# Credits to LeetCode:
# The one and only, DYNAMIC Solution!
# if you know s[i:j] is palindrome then you can check if s[i-1]==s[j+1] is true
# And if yes then it means that s[i-1:j+1] is also a palindrome! (could've used a better indexing but you get the gist)
# Time Complexity = O(n^2)
# Space Complexity = O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # initializing our dynamic table with False
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]
        
        # We know all the substrings of length 1 are palindrome
        # From this we can check the palindromic of odd length of substrings; 3,5,...
        for i in range(n):
            dp[i][i] = True
        
        # For substrings of even length we need to have the s[i:i+1] initialized
        # will stop when it reaches n-1 cause in the loop we'll need to check for i AND i+1
        # and if i was n-1 then i+1 would've been n which is index out of bound (n=len(s))
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        # And from here we'll start checking substrings of length 3,4,5,...,n
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i:j + 1]

################### SOLUTION 2 ######################

# Credits to LeetCode:
# In the first solution checking if a string is palindrome or not was of O(n) complexity and in the second solution if was of O(1).
# In both of the solutions we were working with two indexes, basically we were focused on the bounds of the substring.
# In this solution we will take each element as the center of a possible palindrome and more outward to check if it is a palindrome or not
# This means n centers to check for odd length palindromes and n-1 centers to check for even lengths palindromes. which in total will be O(n)
# Time Complexity = O(n^2)
# Space Complexity = O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            left = i
            right = j
            
            # i and j is the center and wen will work outwards to check for palindromic
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # This will be the length of the palindrome found with i,j being the center
            return right - left - 1
        
        ans = [0, 0]

        # take each of the elements as centers. Both centers of an odd length string and even length string
        for i in range(len(s)):
            odd_length = expand(i, i)
            if odd_length > ans[1] - ans[0] + 1:
                dist = odd_length // 2
                ans = [i - dist, i + dist]

            even_length = expand(i, i + 1)
            if even_length > ans[1] - ans[0] + 1:
                dist = (even_length // 2) - 1
                ans = [i - dist, i + 1 + dist]
                
        i, j = ans
        return s[i:j + 1]
    