class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def s(n):

            res = ["","0"]
            if n == 1:
                return res
            
            for i in range(2, n + 1):
                bef = res[i - 1] + "1"
                aft = ""

                for j in range(len(res[i - 1]) - 1, -1, -1):
                    if res[i - 1][j] == '1':
                        aft += "0"
                    else:
                        aft += "1"
                
                res.append(bef + aft)
            
            return res
        
        out = s(n)
        return out[n][k - 1]