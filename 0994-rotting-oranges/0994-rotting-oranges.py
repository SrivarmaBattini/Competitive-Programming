from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])

        fresh = 0
        queue = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0

        time = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while queue and fresh > 0:
            for _ in range(len(queue)):
                sr, sc = queue.popleft()

                for dr, dc in directions:
                    nr = sr + dr
                    nc = sc + dc

                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in queue and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh -= 1
            
            time += 1

        return time if fresh == 0 else -1