class Solution:
    def reverse(self, x: int) -> int:
        res=0
        k=x
        
        if k<0: k=abs(k)
        while k!=0:
            y=k%10
            res=res*10+y
            k=k//10
               
        if res>(2**31)-1:
            return 0
        elif x>0:
            return res
        else:
            return -1*res
            
    
    
            
        