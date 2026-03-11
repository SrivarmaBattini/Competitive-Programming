class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 0

        res = ""
        while n > 0:
            res += str(n % 2) 
            n = n // 2
        
        ans = 0
        for i in range(len(res)):
            if res[i] == "0":
                ans += (2 ** i)
        
        return ans