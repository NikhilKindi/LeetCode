class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        c={}

        for i in nums:
            if i in c:
                c[i] +=1 
            else:
                c[i] =1 
        for i, j in c.items():
            if j > n//2:
                return i 
        