class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        n = float('inf')
        for str in strs:
            if len(str) < n:
                n = len(str)
        
        for i in range(n):
            char = strs[0][i]
            flag = False
            for j in range(1, len(strs)):
                if char != strs[j][i]:
                    flag = True
                    break
            if not flag:
                res += char
            else:
                break
        return res
                