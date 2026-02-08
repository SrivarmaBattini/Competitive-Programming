class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        
        tokens = s.split()
        num = []

        for token in tokens:
            if token.isnumeric():
                if num:
                    if int(token) <= num[-1]:
                        return False
                num.append(int(token))
        return True