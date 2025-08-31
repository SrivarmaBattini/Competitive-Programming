class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        freq = dict()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                diff = i - j
                if diff in freq:
                    freq[diff].append(matrix[i][j])
                else:
                    freq[diff] = [matrix[i][j]]
                

        for v in freq.values():
            start = v[0]
            for val in v:
                if val != start:
                    return False
        return True
