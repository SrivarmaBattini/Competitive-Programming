class Solution:
    def minOperations(self, s: str) -> int:
        
        n = len(s)
        s1 = ""
        s2 = ""

        for i in range(0, n, 2):
            s1 += "01"
            s2 += "10"

        res1 = 0
        res2 = 0

        for i in range(n):
            if s[i] != s1[i]:
                res1 += 1
            
            if s[i] != s2[i]:
                res2 += 1
        
        return min(res1, res2)