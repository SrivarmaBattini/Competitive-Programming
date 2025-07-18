class Solution:
    def myAtoi(self, s: str) -> int:
        
        posmax = 2 ** 31 - 1
        negmax = - 2 ** 31

        num = ""

        for i in range(len(s)):
            if len(num) == 0 and s[i] == " ":
                continue
            elif len(num) == 0 and (s[i] == "-" or s[i] =="+"):
                num += s[i]
            elif (s[i] == "-" or s[i] =="+") and (num[0] == '+' or num[0] == '-'):
                if i == 1:
                    return 0
                else:
                    break
            elif ord(s[i]) >= 48 and ord(s[i]) <= 57:
                num += s[i]
            else:
                break

        if num == "-" or num == "+" or num == "":
            return 0

        value = int(num)

        if value >= negmax and value <= posmax:
            return value
        elif value < negmax:
            return negmax
        elif value > posmax:
            return posmax 