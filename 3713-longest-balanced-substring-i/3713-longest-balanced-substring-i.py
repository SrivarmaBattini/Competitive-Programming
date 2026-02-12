class Solution:
    def longestBalanced(self, s: str) -> int:
        
        n = len(s)
        res = 0

        for i in range(n):
            freq = {}

            for j in range(i, n):

                freq[s[j]] = freq.setdefault(s[j], 0) + 1

                value = list(freq.values())

                if len(set(value)) == 1:
                    res = max(res, j - i + 1)
        return res