class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:

        visited = set()
        pos = (0, 0)
        last = pos
        m, n = len(grid), len(grid[0])

        while pos not in visited and (0 <= pos[0] < m and 0 <= pos[1] < n):
            visited.add(pos)
            last = pos
            nx, ny = pos
            instruction = grid[nx][ny]

            if instruction == "R":
                ny += 1
            elif instruction == "D":
                nx += 1
            elif instruction == "L":
                ny -= 1
            else:
                nx -= 1

            pos = (nx, ny)

      
        return list(last)