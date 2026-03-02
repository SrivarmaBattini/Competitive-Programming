class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        right_zeros = []

        for row in grid:
            zeros = 0
            for i in range(len(row)-1, -1, -1):
                if row[i] == 0:
                    zeros += 1
                else:
                    break
            right_zeros.append(zeros)
        
        res = 0

        for i in range(len(grid)):

            required_zeros = len(grid) - i - 1
            j = i

            while j < len(grid) and right_zeros[j] < required_zeros:
                j += 1

            if j == len(grid):
                return -1

            while j > i:
                right_zeros[j], right_zeros[j - 1] = right_zeros[j - 1], right_zeros[j] 
                res += 1
                j -= 1
            
        return res
        