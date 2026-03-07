class Solution:
    def minFlips(self, s: str) -> int:
        
        bn = len(s)
        s = s + s
        n = len(s)

        poss1 = ""
        poss2 = ""

        for i in range(0, n):
            if i % 2 == 0:
                poss1 += "0"
                poss2 += "1"
            else:
                poss1 += "1"
                poss2 += "0"
        
        res = float('inf')
        res1 = res2 = 0
        l = 0

        for r in range(n):
            if poss1[r] != s[r]:
                res1 += 1
            if poss2[r] != s[r]:
                res2 += 1
            
            if r - l + 1 > bn:
                if s[l] != poss1[l]:
                    res1 -= 1
                if s[l] != poss2[l]:
                    res2 -= 1
                l += 1
            
            if r - l + 1 == bn:
                res = min(res, res1, res2)
        
        return res