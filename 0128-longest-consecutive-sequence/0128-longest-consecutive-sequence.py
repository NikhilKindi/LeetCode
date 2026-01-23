class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        cnt=0
        l= 1
        if len(s) ==0:
            return 0 
            
        for i in s:
            if i-1 not in s:
                cnt = 1 
                x = i
                while x+1 in s:
                    x=x+1 
                    cnt=cnt+1 

                l= max(l, cnt)
        return l
        