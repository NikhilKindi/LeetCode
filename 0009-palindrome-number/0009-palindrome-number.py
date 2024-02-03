class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev=0
        t=x
        while t>0:
            y=t%10
            rev=rev*10+y
            t=t//10
        if x==rev:
            return True
        elif x<=0:
            return False
        