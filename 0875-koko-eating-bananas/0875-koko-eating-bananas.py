class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low = 1
        high = max(piles)

        while low < high:
            tot = 0
            mid = (low+high)//2
            for t in piles:
                tot += math.ceil(t/mid)
            
            if tot > h:
                low = mid + 1
            else:
                high = mid 
        return low