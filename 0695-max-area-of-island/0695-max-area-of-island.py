from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])

        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visited = set()

        def bfs(sr, sc):

            visited.add((sr, sc))
            queue = deque([(sr, sc)])
            area = 1

            while queue:
                r, c = queue.popleft()

                for dr, dc in direction:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        area += 1
            
            return area
        

        max_area = 0
        for r in range(n):
            for c in range(m):
                if (r, c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))
        
        return max_area