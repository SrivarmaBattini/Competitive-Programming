class Solution:
    def vowelConsonantScore(self, s: str) -> int:

        v = 0
        c = 0
        for char in s:
            if char in ['a','e','i','o','u']:
                v += 1
            elif not char.isalpha():
                continue
            else:
                c += 1

        if c == 0:
            return 0
        else:
            return v // c