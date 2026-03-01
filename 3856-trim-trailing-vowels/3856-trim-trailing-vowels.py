class Solution:
    def trimTrailingVowels(self, s: str) -> str:

        vowels = ['a','e','i','o','u']

        k = -1
        for i in range(len(s)):
            if s[i] not in vowels:
                k = i
        
        return s[:k+1]