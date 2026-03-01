class Solution:
    def minPartitions(self, n: str) -> int:
        
        maxi = 0
        for dig in n:
            maxi = max(maxi, int(dig))
        return maxi