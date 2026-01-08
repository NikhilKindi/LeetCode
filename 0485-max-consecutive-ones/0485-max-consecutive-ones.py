class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        mc=0
        for i in range(n):
            if nums[i] ==1:
                c+=1
            else:
                c=0
            mc= max(mc, c)
        return mc
        