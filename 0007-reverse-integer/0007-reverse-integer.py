class Solution:
    def reverse(self, x: int) -> int:
        
        sx = str(x)
        nsx = ""
        flag = True
        if x < 0:
            flag = False

        for c in sx:
            if c.isdigit():
                nsx += c
            
        res = int(nsx[::-1]) if flag else int(nsx[::-1]) * -1

        if (-2 ** 31) <= res < ((2 ** 31) - 1):
            return res
        else:
            return 0