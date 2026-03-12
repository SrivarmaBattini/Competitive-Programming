class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
            
        start = 1
        last = x // 2

        while start <= last:
            mid = (start+last) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                start = mid + 1
            else:
                last = mid - 1
        
        return last
