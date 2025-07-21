class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        def ishorizontal(grid):
    
            m = len(grid)
            n = len(grid[0])
    
            sum_row = []
            for row in grid:
                s = 0
                for num in row:
                    s += num
                sum_row.append(s)

            total = sum(sum_row)
            for i in range(1, len(sum_row)):
                if sum_row[i - 1] * 2 == total:
                    return True
                else:
                    sum_row[i] = sum_row[i] + sum_row[i-1]

            return False
            # for i in range(1, m):
            #     if sum(sum_row[:i]) == sum(sum_row[i:]):
            #         return True
            #     else:
            #         continue
    
            # return False
    
        def isvertical(grid):
    
            m = len(grid)
            n = len(grid[0])
    
            sum_col = []
    
            for i in range(n):
                s = 0
                for row in grid:
                    s += row[i]
                sum_col.append(s)

            total = sum(sum_col)
            for i in range(1, len(sum_col)):
                if sum_col[i - 1] * 2 == total:
                    return True
                else:
                    sum_col[i] = sum_col[i] + sum_col[i-1]

            return False
            # for i in range(1, len(sum_col)):
            #     if sum(sum_col[:i]) == sum(sum_col[i:]):
            #         return True
            #     else:
            #         continue
    
            # return False

        if ishorizontal(grid) or isvertical(grid):
            return True
        else:
            return False
            
                