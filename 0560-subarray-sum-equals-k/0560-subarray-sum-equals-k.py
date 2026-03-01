class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        pref = 0
        res = 0

        freq = {0 : 1}

        for num in nums:
            pref += num

            if pref - k in freq:
                res += freq[pref - k]
            
            freq[pref] = freq.setdefault(pref, 0) + 1
        
        return res