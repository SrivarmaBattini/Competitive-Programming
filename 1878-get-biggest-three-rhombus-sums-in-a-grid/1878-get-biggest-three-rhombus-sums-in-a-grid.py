class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
    
        m = len(grid)
        n = len(grid[0])
        total = set()    

        for r in range(m):
            for c in range(n):
                
                total.add(grid[r][c])
                k = 1
                while True:
                    if r-k < 0 or r+k >= m or c-k < 0 or c+k >= n:
                        break

                    s = 0

                    for i in range(k):
                        s += grid[r-k+i][c+i]
                        s += grid[r+i][c+k-i]
                        s += grid[r+k-i][c-i]
                        s += grid[r-i][c-k+i]
                
                    total.add(s)
                    k += 1
        return sorted(total, reverse = True)[:3]

        # for i in range(m):
        #     for j in range(n):
        #         total.add(grid[i][j])
        
        # if (m < 3 and n <= 3) or (m <= 3 and n < 3):
        #     first = max(total)
        #     total.remove(first)
        #     if total:
        #         second = max(total)
        #         total.remove(second)
        #         if total:
        #             third = max(total)
        #             return [first,second,third]
        #         else:
        #             return [first,second]
        #     else:
        #         return [first]
        
        # for i in range(1, m-1):
        #     for j in range(1, n-1):
        #         summ = grid[i-1][j] + grid[i][j-1] + grid[i+1][j] + grid[i][j+1]
        #         total.add(summ)
        
        # first = max(total)
        # total.remove(first)
        # print(total)

        # if total:
        #     second = max(total)
        #     total.remove(second)
        #     if total:
        #         third = max(total)
        #         return [first,second,third]
        #     else:
        #         return [first,second]
        # else:
        #     return [first]