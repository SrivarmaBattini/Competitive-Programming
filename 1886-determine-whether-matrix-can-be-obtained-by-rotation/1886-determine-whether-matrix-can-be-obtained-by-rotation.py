class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(grid, tar):
            m = len(grid)
            matrix = [[0]*m for _ in range(m)]
            
            for i in range(m):
                k = 0
                for j in range(m-1, -1, -1):
                    matrix[i][k] = grid[j][i]
                    k += 1
            
            for i in range(m):
                for j in range(m):
                    if matrix[i][j] != tar[i][j]:
                        return False, matrix
            return True, matrix
        
        for i in range(4):
            flag, mat = rotate(mat, target)
            if flag:
                return True
        return False