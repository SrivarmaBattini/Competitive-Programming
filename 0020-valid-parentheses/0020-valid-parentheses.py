class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        pairs = {']' : '[', ')' : '(', '}' : '{'}

        for c in s:
            if c in '({[':
                stack.append(c)
            elif c in ')}]':
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                continue
        return len(stack) == 0