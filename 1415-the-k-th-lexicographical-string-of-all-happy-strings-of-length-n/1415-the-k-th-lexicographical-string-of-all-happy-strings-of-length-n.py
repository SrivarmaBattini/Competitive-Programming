class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        happy = ['a', 'b', 'c']
        poss = 3 * (2 ** (n-1))
        if k > poss:
            return ""
        if n == 1:
            return happy[k-1] if 0 < k < 4 else ""
        
        res = ""
        for i in range(n):
            for c in happy:
                if res and res[-1] == c:
                    continue
                
                rem = n - i - 1
                count = 2 ** rem

                if k > count:
                    k -= count
                else:
                    res += c
                    break
        return res