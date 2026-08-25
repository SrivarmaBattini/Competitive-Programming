class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        carry = 0
        i = j = 0
        m = len(a)
        n = len(b)
        a = a[::-1]
        b = b[::-1]
        res = ""

        while i < m or j < n or carry > 0:
            n1 = int(a[i]) if i < m else 0
            n2 = int(b[j]) if j < n else 0
            tot = n1 + n2 + carry

            res += str(tot % 2)
            carry = tot // 2
            i += 1
            j += 1
        return res[::-1]