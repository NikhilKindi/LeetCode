class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        h=len(haystack)
        if needle=="":
            return 0
        
        for i in range(h+1-n):
            if haystack[i:i+n]==needle:
                return i
        return -1
            
        