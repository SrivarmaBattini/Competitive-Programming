class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        if len(palindrome) == 1:
            return ""
        
        i = 0
        j = len(palindrome) - 1

        while i < j:
            if palindrome[i] != "a" and palindrome[j] != "a":
                return palindrome[:i] + "a" + palindrome[i+1:]
            else:
                i += 1
                j -= 1
        return palindrome[:-1] + "b"