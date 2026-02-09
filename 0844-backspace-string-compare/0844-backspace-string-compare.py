class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        sl = []
        for ch in s:
            if ch == '#':
                if sl:
                    sl.pop()
            else:
                sl.append(ch)
        
        tl = []
        for ch in t:
            if ch == '#':
                if tl:
                    tl.pop()
            else:
                tl.append(ch)
        
        return "".join(sl) == "".join(tl)
            