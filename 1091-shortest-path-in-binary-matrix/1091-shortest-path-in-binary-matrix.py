from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        m = len(grid)
        n = len(grid[0])

        if n == 1:
            return 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        visited = set()

        visited.add((0,0))
        queue = deque([(0, 0, 1)])

        while queue:
            r, c, dist = queue.popleft()

            if (r, c) == (m-1, n-1):
                return dist
            
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))
        
        return -1