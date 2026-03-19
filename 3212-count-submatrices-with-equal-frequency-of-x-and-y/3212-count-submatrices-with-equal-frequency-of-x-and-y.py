class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        dpx = [0] * n
        dpy = [0] * n
        res = 0

        for i in range(m):
            x = 0
            y = 0
            for j in range(n):
                if grid[i][j] == 'X':
                    x += 1
                elif grid[i][j] == 'Y':
                    y += 1
                
                dpx[j] += x
                dpy[j] += y
                if dpx[j] > 0 and dpx[j] == dpy[j]:
                    res += 1

        return res