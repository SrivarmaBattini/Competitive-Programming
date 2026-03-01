class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        if sum(nums) < target:
            return 0

        i = j = 0
        total = nums[i]
        res = len(nums)

        while j < len(nums):
            if total >= target:
                res = min(res, j - i + 1)
                total -= nums[i]
                i += 1
            else:
                j += 1
                if j < len(nums):
                    total += nums[j] 
        
        return res