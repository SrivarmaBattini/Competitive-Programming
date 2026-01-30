class Solution:
    def minSteps(self, s: str, t: str) -> int:

        freq1 = {}
        for char in s:
            freq1[char] = freq1.setdefault(char, 0) + 1

        freq2 = {}
        for char in t:
            freq2[char] = freq2.setdefault(char, 0) + 1

        res = 0
        
        for u, v in freq1.items():
            if u not in freq2:
                res += v
            else:
                res += abs(freq1[u] - freq2[u])

        for u, v in freq2.items():
            if u not in freq1:
                res += v
        
        return res