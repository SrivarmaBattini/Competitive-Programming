class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        
        # n = len(nums)
        
        # a = max(nums)
        # b = min(nums)

        # a_count = nums.count(a)

        # if a_count > n // 2:
        #     return 2 * a
        # elif a_count == n // 2:
        #     nums.removeall(a)
        #     return max(a) + b
        # elif 
        # return a + b

        n = len(nums)
        nums.sort()

        res = 0
        for i in range(n // 2):
            res = max(res, nums[i] + nums[n - i - 1])
        
        return res