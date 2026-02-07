class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        res = 0
        rem = 0

        for char in s:
            if char == 'b':
                rem += 1
            elif rem:
                res += 1
                rem -= 1
        return res