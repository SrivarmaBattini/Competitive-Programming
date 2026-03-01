class Solution:
    def minCost(self, n: int) -> int:

        def costs(n):
            res = [0, 0, 1, 3]

            if n <= 3:
                return res[n]
                
            for j in range(4, n+1):
                if j % 2 == 0:
                    i = j // 2
                    res.append(((i**2) + (res[i]*2)))
                else:
                    i = j // 2
                    res.append(((i*(i+1)) + res[i] + res[i+1]))
          
            return res[-1]

        return costs(n)