class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowel = ['a','A','e','E','i','I','o','O','u','U']

        i = 0
        j = len(s) - 1
        res = [char for char in s]

        while i < j:

            while s[i] not in vowel and i < j:
                i += 1
            
            while s[j] not in vowel and j > i:
                j -= 1
            
            res[i], res[j] = res[j], res[i]
            i += 1
            j -= 1
        
        return "".join(res)