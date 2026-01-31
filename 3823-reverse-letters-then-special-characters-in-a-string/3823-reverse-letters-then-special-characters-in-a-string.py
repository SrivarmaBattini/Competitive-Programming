class Solution:
    def reverseByType(self, s: str) -> str:

        sc = []
        si = []
        ac = []
        ai = []

        for i, c in enumerate(s):
            if 97 <= ord(c) <= 122:
                ac.append(c)
                ai.append(i)
            else:
                sc.append(c)
                si.append(i)


        ac.reverse()
        sc.reverse()
        
        res = ""
        for i in range(len(s)):
            if i in ai:
                res = res + str(ac[ai.index(i)])

            if i in si:
                res = res + str(sc[si.index(i)])

        return res