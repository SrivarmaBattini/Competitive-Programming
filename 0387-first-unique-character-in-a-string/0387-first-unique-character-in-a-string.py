class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        val = ""
        for u, v in freq.items():
            if v == 1:
               val = u
               break

        if val == "":
            return -1
        else:
            return s.index(val)