class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        j=1
        while(j<len(nums)):
            if nums[i]!=nums[j]:
                i+=1
                j+=1
            elif nums[i]==nums[j]:
                nums.pop(j)
            
                
            
        