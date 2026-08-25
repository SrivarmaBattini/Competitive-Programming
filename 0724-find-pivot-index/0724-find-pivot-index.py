class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        left_sum = [nums[0]] * n

        for i in range(1, n):
            left_sum[i] = nums[i] + left_sum[i-1]
        
        left_sum = [0] + left_sum
        sum = 0

        for i in range(n):
            sum += nums[i]
        
        for i in range(1, len(left_sum)):
            if left_sum[i-1] == (sum - left_sum[i]):
                return i - 1
        return -1