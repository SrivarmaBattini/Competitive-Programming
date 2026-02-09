class Solution:
    def removeStars(self, s: str) -> str:
        
        j = 0
        res = []

        for j in range(len(s)):
            if s[j] == '*' and res:
                res.pop()
            elif s[j] != '*':
                res.append(s[j])
        
        return "".join(res)
                