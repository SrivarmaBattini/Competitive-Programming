class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        if not matrix:
            return res

        m = len(matrix)
        n = len(matrix[0])

        i = 0
        k = m
        l = n

        while i < k and i < l:
            for x in range(i, l):
                res.append(matrix[i][x])
            
            for y in range(i+1, k):
                res.append(matrix[y][l-1])
            
            if i < k-1:
                for z in range(l-2, i-1, -1):
                    res.append(matrix[k-1][z])
            
            if i < l-1:
                for j in range(k-2, i, -1):
                    res.append(matrix[j][i])

            i += 1
            k -= 1
            l -= 1

        return res
