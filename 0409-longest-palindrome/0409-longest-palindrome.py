class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        freq = dict()

        for char in s:
            freq[char] = freq.setdefault(char, 0) + 1

        values = []
        for u, v in freq.items():
            values.append(v)

        values.sort(reverse = True)
        i = 0
        out = 0

        for val in values:
            if val % 2 == 0:
                out += val
            elif val % 2 == 1 and i == 0:
                i += 1
                out += val
            else:
                out += val - 1
                i += 1
        return out


