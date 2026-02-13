class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        freq = dict()

        for num in nums:
            freq[num] = freq.setdefault(num, 0) + 1
        
        value = sorted(list(freq.keys()))

        if len(value) < 3:
            return value[-1]
        return value[len(value) - 3]