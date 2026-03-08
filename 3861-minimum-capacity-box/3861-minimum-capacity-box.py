class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        
        idx = -1
        ans = float('inf')
        for i in range(len(capacity)):
            if capacity[i] >= itemSize:
                if capacity[i] < ans:
                    idx = i
                    ans = capacity[i]
        return idx