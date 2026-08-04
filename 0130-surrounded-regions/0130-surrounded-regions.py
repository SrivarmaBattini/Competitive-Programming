from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        direction = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        n = len(board)
        m = len(board[0])

        def bfs(sr, sc):
            queue = deque([(sr, sc)])
            visited.add((sr, sc))

            while queue:
                r, c = queue.popleft()

                for dr, dc in direction:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and board[nr][nc] == "O":
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        

        for i in range(n):
            for j in range(m):
                if i == 0 or i == n-1:
                    if board[i][j] == "O":
                        bfs(i, j)
                else:
                    if board[i][j] == "O" and (j == 0 or j == m - 1):
                        bfs(i, j)
        

        for i in range(n):
            for j in range(m):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"
        