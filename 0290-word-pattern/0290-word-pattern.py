class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        freq1 = dict()
        freq2 = dict()
        ss = s.split()

        if len(ss) != len(pattern):
            return False

        if len(s) == len(pattern) == 0:
            return True

        for i in range(len(pattern)):
            char = pattern[i]
            word = ss[i]

            if char in freq1:
                if freq1[char] != word:
                    return False
            else:
                freq1[char] = word

            if word in freq2:
                if freq2[word] != char:
                    return False
            else:
                freq2[word] = char

        return True