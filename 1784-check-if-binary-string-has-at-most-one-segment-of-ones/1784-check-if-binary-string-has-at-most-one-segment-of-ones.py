class Solution:
    def checkOnesSegment(self, s: str) -> bool:

        if s[0] == "0":
            return False

        if len(s) == 1:
            return True
        
        i = 0
        while i < len(s):
            if s[i] == "0":
                break
            i += 1

        for j in range(i, len(s)):
            if s[j] == "1":
                return False
        return True