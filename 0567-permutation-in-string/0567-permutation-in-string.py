class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        for c in s1:
            need[ord(c) - ord('a')] += 1
        
        n = len(s1)
        m = len(s2)
        for i in range(m):
            window[ord(s2[i]) - ord('a')] += 1
            if i >= n:
                window[ord(s2[i-n]) - ord('a')] -= 1
            if window == need:
                return True
        return False