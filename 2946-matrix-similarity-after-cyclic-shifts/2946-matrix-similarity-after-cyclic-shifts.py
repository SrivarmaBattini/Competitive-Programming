class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        m = len(mat)
        n = len(mat[0])

        res = []
        for i in range(m):
            if i % 2 == 0:
                res.append(mat[i][k%n:] + mat[i][:k%n])
            else:
                res.append(mat[i][n - (k%n):] + mat[i][:n - (k%n)])
        
        return mat == res