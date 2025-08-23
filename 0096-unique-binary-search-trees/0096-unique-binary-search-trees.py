class Solution:
    def numTrees(self, n: int) -> int:

        numerator = 1
        for i in range(1,(2*n)+1):
            numerator *= i
        
        r = 1
        for i in range(1,n+1):
            r *= i
        
        return numerator // (r*r*(n+1))

        