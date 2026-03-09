#from functools import lru_cache

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [[[0]*2 for _ in range(one+1)] for _ in range(zero+1)]

        for i in range(1, min(zero, limit)+1):
            dp[i][0][0] = 1
        
        for j in range(1, min(one, limit)+1):
            dp[0][j][1] = 1
        

        for i in range(1, zero+1):
            for j in range(1, one+1):
                if i > 0:
                    val = dp[i-1][j][0] + dp[i-1][j][1]
                    
                    if i-limit-1 >= 0:
                        val -= dp[i-limit-1][j][1]
                    dp[i][j][0] = (dp[i][j][0] + val + MOD) % MOD
                
                if j > 0:
                    val = dp[i][j-1][0] + dp[i][j-1][1]

                    if j-limit-1 >= 0:
                        val -= dp[i][j-limit-1][0]
                    dp[i][j][1] = (dp[i][j][1] + val + MOD) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD


        # @lru_cache(None)
        # def dp(z, o, last, count):
        #     if z == 0 and o == 0:
        #         return 1
            
        #     ans = 0

        #     if z > 0:
        #         if last == 0:
        #             if count < limit:
        #                 ans += dp(z-1, o, 0, count+1)
        #         else:
        #             ans += dp(z-1, o, 0, 1)
            
        #     if o > 0:
        #         if last == 1:
        #             if count < limit:
        #                 ans += dp(z, o-1, 1, count+1)
        #         else:
        #             ans += dp(z, o-1, 1, 1)
            
        #     return ans % MOD
        
        # return dp(zero, one, -1, 0)