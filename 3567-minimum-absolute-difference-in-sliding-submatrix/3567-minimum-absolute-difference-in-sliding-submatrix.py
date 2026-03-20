class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        res = [[0] * (n-k+1) for _ in range(m-k+1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                v = sorted(set(grid[x][y] for x in range(i, i+k) for y in range(j, j+k)))

                if len(v) <= 1:
                    res[i][j] = 0
                else:
                    res[i][j] = min(v[p+1] - v[p] for p in range(len(v) - 1))
        return res