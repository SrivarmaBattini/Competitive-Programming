class Solution:
    def canAliceWin(self, n: int) -> bool:
        
        win = 0
        r = 10

        while n >= 0:
            n -= r
            if n < 0 and win == 0:
                return False
            elif n >= 0:
                if win == 0:
                    win = 1
                else:
                    win = 0
            r -= 1
        return True