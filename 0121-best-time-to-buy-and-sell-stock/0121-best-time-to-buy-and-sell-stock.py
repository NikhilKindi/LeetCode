class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        m1=float('-inf')
        m=min(prices)
        n=len(prices)
        res=0
        if m == prices[n-1]:
            return 0 
        for i in range(prices.index(m)+1,n):
            if prices[i]> m1:
                m1 = prices[i]
        res= m1-m
        return res 
        '''
        mprof= 0 
        minprice=float('inf')

        for i in prices:
            if i < minprice:
                minprice= i 
            else:
                mprof= max(mprof, i-minprice)
        return mprof
        