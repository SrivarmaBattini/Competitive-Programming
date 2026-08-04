from collections import deque
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        
        visited = set()
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        def bfs(sr, sc):

            visited.add((sr, sc))
            queue = deque([(sr, sc)])

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        

        for r in range(m):
            for c in range(n):
                if r == 0 or r == m - 1:
                    if grid[r][c] == 1:
                        bfs(r, c)
                else:
                    if (c == 0 or c == n-1) and grid[r][c] == 1:
                        bfs(r, c)
        
        land = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    land += 1
        
        return land