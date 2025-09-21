class Solution:
    def reverseWords(self, s: str) -> str:
        
        res = ""
        i = len(s) - 1
        j = len(s)

        while i >= 0:
            
            while i >= 0 and s[i] == " ":
                i -= 1
            j = i + 1

            while i >= 0 and s[i] != " ":
                i -= 1

            if j > 0:
                if res:
                    res += " "
                res += s[i+1:j]

        return res