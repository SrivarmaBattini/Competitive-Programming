class Solution:
    def checkString(self, s: str) -> bool:
        
        count = 0
        for char in s:
            if char == 'b':
                count += 1
            elif count:
                return False
        return True