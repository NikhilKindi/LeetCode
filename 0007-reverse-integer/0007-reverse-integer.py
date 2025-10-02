class Solution:
    def reverse(self, x: int) -> int:
        k=x
        d=0
        if k<0:
            k=abs(k)
        while k!=0:
            r= k % 10
            d = r + 10 * d
            k= k//10

        if d> (2**31)-1:
            return 0
        elif x>0:
            return d
        else:
            return -1*d

        