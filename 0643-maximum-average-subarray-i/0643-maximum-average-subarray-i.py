class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        res = float('-inf')
        val = 0
        for i in range(len(nums)):
            if i < k - 1:
                val += nums[i]
            elif i > k - 1:
                val += (nums[i] - nums[i - k])
                res = max(res, val/k)
            else:
                val += nums[i]
                res = max(res, val/k)
        
        return res