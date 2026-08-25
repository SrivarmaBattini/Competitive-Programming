class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        s = "".join(map(str, digits))
        si = int(s)
        sinc = si + 1
        ssinc = str(sinc)
        return list(map(int, ssinc))