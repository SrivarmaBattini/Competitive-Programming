class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x == 0 and n <= 0:
            raise ValueError("Undefined: 0 cannot be raised to zero or a negative power")
        return x ** n
