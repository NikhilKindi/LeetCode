class Solution:
    def hammingWeight(self, n: int) -> int:

        b= format(n,'b')
        l=list(b)
        c=0
        for i in range(len(l)):
            if l[i] == '1':
                c+=1 
            
        return c


        