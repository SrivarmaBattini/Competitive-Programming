class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        res = []
        n = len(s)

        for i in range(0, n, 2*k):

            res.append(s[i:i+k][::-1])
            res.append(s[i+k:i+2*k])
        
        return "".join(res)