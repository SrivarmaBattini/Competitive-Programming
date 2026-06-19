class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        lin_res = curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])
            lin_res = max(lin_res, curr)

        curr = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            if curr < 0:
                if curr + nums[i] > 0:
                    curr = nums[i]
                else:
                    curr = curr + nums[i]
            else:
                curr = nums[i]

            res = min(curr, res)

        if sum(nums) == res: return lin_res
        return max(lin_res, (sum(nums)-res))