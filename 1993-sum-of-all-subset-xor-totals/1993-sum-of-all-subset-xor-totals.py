from itertools import combinations
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        res = 0
        n = len(nums)
        for num in nums:
            res |= num
        return res * (1 << n-1)