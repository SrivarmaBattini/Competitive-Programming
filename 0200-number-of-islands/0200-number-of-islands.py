from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = set()
        move = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        islands = 0

        n = len(grid)
        m = len(grid[0])


        def bfs(sr, sc):
            queue = deque([(sr, sc)])
            visited.add((sr, sc))

            while queue:
                r, c = queue.popleft()

                for dr, dc in move:
                    nr = r + dr
                    nc = c + dc
                    
                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and grid[nr][nc] == "1":
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        for sr in range(n):
            for sc in range(m):
                if grid[sr][sc] == "1" and (sr, sc) not in visited:
                    islands += 1
                    bfs(sr, sc)
        
        return islands