class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        for i in range(x, x + (k//2)):
            for j in range(y, y + k):
                opposite = 2 * x + k - 1 - i
                grid[i][j], grid[opposite][j] = grid[opposite][j], grid[i][j]
        return grid