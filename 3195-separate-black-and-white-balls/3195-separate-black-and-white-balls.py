class Solution:
    def minimumSteps(self, s: str) -> int:
        
        j = 0
        k = 0
        res = 0
        while j < len(s):
            if s[j] == '1':
                k += 1
            else:
                res += k
            j += 1
        return res 