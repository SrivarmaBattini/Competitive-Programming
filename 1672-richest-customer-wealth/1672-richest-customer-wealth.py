class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        wealth = 0
        for acc in accounts:
            total = 0
            for money in acc:
                total += money
            
            if wealth < total:
                wealth = total
        
        return wealth
