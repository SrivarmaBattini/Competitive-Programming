class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        m = len(grid[0])
        matrix = dict()

        for i in range(n):
            for j in range(m):

                val = i - j
                if val not in matrix:
                    matrix[val] = [grid[i][j]]
                else:
                    matrix[val].append(grid[i][j])
        
        for val, diag in matrix.items():
            if val < 0:
                diag.sort()
            else:
                diag.sort(reverse = True)
        
        for i in range(n):
            for j in range(m):
                val = i - j
                grid[i][j] = matrix[val].pop(0)
        
        return grid