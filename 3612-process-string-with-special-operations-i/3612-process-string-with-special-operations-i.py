class Solution:
    def processStr(self, s: str) -> str:
        
        ans = ""
        for char in s:
            if char == '*':
                if ans:
                    ans = ans[:-1]
            elif char == '#':
                ans *= 2
            elif char == '%':
                ans = ans[::-1]
            else:
                ans += char
        return ans