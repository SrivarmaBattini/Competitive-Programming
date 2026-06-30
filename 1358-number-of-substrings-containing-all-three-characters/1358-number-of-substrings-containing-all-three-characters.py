class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        count = {'a':0, 'b':0, 'c':0}
        i = 0
        ans = 0
        
        for j in range(len(s)):
            count[s[j]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += len(s) - j

                count[s[i]] -= 1
                i += 1
        
        return ans