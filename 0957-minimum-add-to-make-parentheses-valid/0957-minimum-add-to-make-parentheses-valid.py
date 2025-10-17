class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []

        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                elif not stack or stack[-1] == c:
                    stack.append(c)
                else:
                    stack.append(c)
        return len(stack)
