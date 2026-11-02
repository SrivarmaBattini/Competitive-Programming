class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        
        nums.sort()
        n = len(nums)
        idx = n // 2

        res = 0
        for i in range(n):
            res += abs(nums[i] - nums[idx])
        
        return res