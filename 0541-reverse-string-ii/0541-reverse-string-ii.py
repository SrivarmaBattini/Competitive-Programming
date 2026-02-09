class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        # res = []
        # n = len(s)

        # for i in range(0, n, 2*k):

        #     res.append(s[i:i+k][::-1])
        #     res.append(s[i+k:i+2*k])
        
        # return "".join(res)

        def fun(ss):
            
            out = ""
            m = min(k, len(ss))
            for i in range(len(ss)):
                if i < m:
                    out += ss[m - i - 1]
                else:
                    out += ss[i]
            return out

        res = ""
        for i in range(0, len(s), 2*k):
            ns = fun(s[i:min(i+2*k,len(s))])
            res += ns

        return res

        