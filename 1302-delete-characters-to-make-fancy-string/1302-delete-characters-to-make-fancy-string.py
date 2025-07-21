class Solution:
    def makeFancyString(self, s: str) -> str:
        
        if len(s) <= 2:
            return s
        res = s[0]
        j = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                j += 1
            else:
                j = 1
            
            if j < 3:
                res += s[i]
            
        return res