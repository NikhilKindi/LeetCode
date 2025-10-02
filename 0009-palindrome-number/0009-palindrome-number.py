class Solution:
    def isPalindrome(self, x: int) -> bool:
        while x<0:
            return False
        
        k=x
        d=0
        while k!=0:
            r=k%10
            d= r+10*d
            k=k//10

        if d==x:
            return True
        else:
            return False
            

        
        