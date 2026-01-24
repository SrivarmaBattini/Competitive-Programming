class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = sorted(nums)

        res = 0
        for i in range(n // 2):
            res = max(res, nums[i] + nums[n - i - 1])
        
        return res