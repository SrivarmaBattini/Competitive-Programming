class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        m = len(grid) 
        n = len(grid[0])

        output = [[1] * n for _ in range(m)]

        prefix = 1
        for i in range(m):
            for j in range(n):
                output[i][j] = prefix
                prefix = (grid[i][j] * prefix) % 12345
        
        suffix = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                output[i][j] = (output[i][j] * suffix) % 12345
                suffix = (suffix * grid[i][j]) % 12345
        
        return output

        # pro = 1
        # for row in grid:
        #     for num in row:
        #         pro *= num
        
        # m = len(grid)
        # n = len(grid[0])
        # output = [[0] * n for _ in range(m)]

        # for i in range(m):
        #     for j in range(n):
        #         output[i][j] = (pro // grid[i][j]) % 12345
        
        # return output