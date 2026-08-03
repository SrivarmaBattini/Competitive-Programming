from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        n = len(stoneValue)

        @lru_cache(maxsize=None)
        def dfs(i):
            if i >= n:
                return 0

            ans = float('-inf')
            curr = 0

            for k in range(3):
                if i + k < n:
                    curr += stoneValue[i+k]
                    ans = max(ans, curr - dfs(i+k+1))

            return ans
        

        res = dfs(0)
        if res < 0:
            return "Bob"
        elif res == 0:
            return "Tie"
        else:
            return "Alice"