class Solution:
    def countValidSubstrings(self, s: str) -> int:

        n = len(s)
        res = 0
        abc = -1

        for i in range(n):
            if i >= 2 and s[i-2:i+1] == "abc":
                abc = i - 2

            res += i - abc

        return res
        