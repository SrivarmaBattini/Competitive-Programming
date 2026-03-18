class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        
        m = len(grid)
        n = len(grid[0])

        total = [[0]*n for i in range(m)]
        for i in range(n):
            if i == 0:
                total[0][i] = grid[0][0]
            else:
                total[0][i] = grid[0][i] + total[0][i-1]
        
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    total[i][j] = grid[i][j] + total[i-1][j]
                else:
                    total[i][j] =  grid[i][j] + total[i-1][j] + total[i][j-1] - total[i-1][j-1]
        
        print(total)
        res = 0
        for lt in total:
            for val in lt:
                if val <= k:
                    res += 1
        return res