class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = dict()

        for char in s:
            freq[char] = freq.setdefault(char, 0) + 1

        rep = list(freq.values())
        output = 0
        while len(rep) > k:
            min_val = min(rep)
            output += min_val
            rep.remove(min_val)

        return output