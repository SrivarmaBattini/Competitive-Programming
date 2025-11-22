class Solution:
    def minimumFlips(self, n: int) -> int:
        def binary(n):
            s = ""
            while n > 0:
                s = str(n % 2) + s
                n = n//2
            return s

        s = binary(n)
        if len(s) == 1:
            return 0

        flips = 0
        i = 0
        j = len(s) - 1

        while i < j:
            if s[i] != s[j]:
                flips += 2
            i += 1
            j -= 1

        return flips