class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        
        res = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()

        for i in range(m):
            x = len(visited)
            for j in range(n):
                if grid[i][j] == 1:
                    visited.add((i, j))
            
            if len(visited) - x > 1:
                res += len(visited) - x
            else:
                for k in range(n):
                    if grid[i][k] == 1:
                        visited.remove((i, k))
                        break
        
        for i in range(n):
            count = 0
            rep = 0
            for j in range(m):
                if (j, i) in visited:
                    rep += 1
                
                if grid[j][i] == 1:
                    count += 1
            
            if count >= 2:
                res += count - rep
        
        return res