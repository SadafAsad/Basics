class Solution:
    def longestPalindrome(self, s:str) -> str:
        max_tmp = ""
        start_index_tmp = 0
        while start_index_tmp<len(s):
            max_s = ""
            start_index = start_index_tmp
            end_index = len(s)-1
            counter = 0
            while start_index<end_index:
                if s[start_index]==s[end_index]:
                    max_s+=s[start_index]
                    start_index+=1
                    end_index-=1
                else:
                    counter+=1
                    max_s = ""
                    start_index = start_index_tmp
                    end_index = len(s)-1-counter
            
            odd = False
            if start_index==end_index:
                odd = True
                max_s+=s[start_index]
            
            i = len(max_s)-2 if odd else len(max_s)-1
            while i>=0:
                max_s+=max_s[i]
                i-=1
            
            if len(max_tmp)<len(max_s):
                max_tmp = max_s
            start_index_tmp+=1
        return max_tmp