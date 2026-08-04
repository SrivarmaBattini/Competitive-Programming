from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        visited = set()
        start_pixel = image[sr][sc]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(r, c):

            visited.add((r, c))
            queue = deque([(r, c)])

            while queue:
                cr, cc = queue.popleft()
                image[cr][cc] = color
                for dr, dc in directions:
                    nr = cr + dr
                    nc = cc + dc

                    if 0 <= nr < m and 0 <= nc < n and image[nr][nc] == start_pixel and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        
        bfs(sr, sc)
        return image