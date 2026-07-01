class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        if c == 0: return True
        for i in range(int(c**0.5)+1):
            rem = c - (i * i)
            b = int(rem**0.5)
            if b ** 2 == rem:
                return True
        return False