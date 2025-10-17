class Solution:
    def minSwaps(self, s: str) -> int:
        balance = 0
        max_bal = 0

        for c in s:
            if c == '[':
                balance += 1
            elif c == ']':
                balance -= 1
            
            if balance < 0:
                max_bal = max(max_bal, -balance)
        
        return (max_bal + 1) // 2