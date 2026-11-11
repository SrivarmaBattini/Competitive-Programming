class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        if need1 > need2:
            return min(costBoth * max(need1, need2), (costBoth * need2) + (cost1 * (need1 - need2)), cost1*need1 + cost2*need2)
        else:
            return min(costBoth * max(need1, need2), (costBoth * need1) + (cost2 * (need2 - need1)), cost1*need1 + cost2*need2)