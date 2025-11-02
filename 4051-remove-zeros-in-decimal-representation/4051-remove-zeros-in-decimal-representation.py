class Solution:
    def removeZeros(self, n: int) -> int:

        res = ""
        for s in str(n):
            if s == "0":
                continue
            else:
                res += s

        return int(res) if res else None