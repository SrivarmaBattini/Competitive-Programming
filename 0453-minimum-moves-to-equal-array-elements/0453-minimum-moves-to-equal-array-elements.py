class Solution:
    def minMoves(self, nums: list[int]) -> int:
        
        res = 0
        min_e = min(nums)

        for i in range(len(nums)):
            res += (nums[i] - min_e)
        
        return res