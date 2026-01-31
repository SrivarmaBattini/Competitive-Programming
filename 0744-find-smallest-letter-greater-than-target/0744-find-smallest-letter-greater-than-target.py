class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        tar = ord(target) - 97
        flag = False

        for letter in letters:
            if (ord(letter) - 97) > tar:
                return letter
            else:
                flag = False
        
        if flag is False:
            return letters[0]