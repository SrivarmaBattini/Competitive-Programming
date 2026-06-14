class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        res = ""

        for word in words:
            total = 0
            for char in word:
                total += weights[ord(char)-97]
            
            pos = total % 26
            res += chr(97 + 25 - pos)
        
        return res
