class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        for i in range(n, n + t + 1):
            prod = 1
            num = i
            while num:
                prod *= (num%10)
                num //= 10
            
            if prod % t == 0:
                return i