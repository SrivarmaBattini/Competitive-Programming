class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        res = [[0] * n for _ in range(n)]
        input_val = [num for num in range(1,n*n+1)]

        
        k = 0       # row pointer
        m = 0       # left boundary
        o = n       # right/bottom boundary
        
        for _ in range(n, 0, -1):   
            
            # left to right
            for j in range(m, o):
                if input_val:
                    res[k][j] = input_val.pop(0)
            
            # top to bottom
            for i in range(k+1, o):
                if input_val:
                    res[i][o-1] = input_val.pop(0)
            
            # right to left
            for j in range(o-2, m-1, -1):
                if input_val:
                    res[o-1][j] = input_val.pop(0)
            
            # bottom to top
            for i in range(o-2, k, -1):
                if input_val:
                    res[i][m] = input_val.pop(0)

            k += 1
            m += 1
            o -= 1
        
        return res
