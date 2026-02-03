class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        res = []
        stack = []

        for i in range(9, 0, -1):
            stack.append(i)
        
        while stack:
            val = stack.pop()
            if val > n:
                continue 
                
            res.append(val)

            for i in range(9, -1, -1):
                curr = val * 10 + i
                if curr <= n:
                    stack.append(curr)
        return res