class Solution:
    def trimTrailingVowels(self, s: str) -> str:

        k = -1
        for i in range(len(s)):
            if s[i] not in "aeiou":
                k = i
        
        return s[:k+1]