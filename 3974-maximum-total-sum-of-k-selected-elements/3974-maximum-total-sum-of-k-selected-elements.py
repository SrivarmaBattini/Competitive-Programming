class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:

        nums.sort()
        res = 0 
        n = len(nums)

        for i in range(k):
            if mul>1:
                res += (mul * nums[n - i - 1])
                mul -= 1
            else:
                res += nums[n - i - 1]

        return res