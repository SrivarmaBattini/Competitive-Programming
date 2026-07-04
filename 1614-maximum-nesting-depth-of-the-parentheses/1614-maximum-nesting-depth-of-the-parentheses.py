class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = []
        max_count = 0
        for c in s:
            if c == "(":
                stack.append("(")
            elif c == ")":
                stack.pop()
            else:
                continue
            max_count = max(max_count, len(stack))
        return max_count