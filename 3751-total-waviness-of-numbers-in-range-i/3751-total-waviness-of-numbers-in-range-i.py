class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def waviness(num):
            s = str(num)
            if len(s) < 3:
                return 0

            w = 0
            for i in range(1, len(s) - 1):
                a, b, c = s[i-1], s[i], s[i+1]

                if b > a and b > c:
                    w += 1
                if b < a and b < c:
                    w += 1
            return w
                    
        total = 0
        for num in range(num1, num2 + 1):
            total += waviness(num)
        return total