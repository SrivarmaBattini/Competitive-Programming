class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)

        pro = nums[0]
        for i in range(1, len(nums)):
            res[i] = pro
            pro *= nums[i]
        
        pro = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] = res[i] * pro
            pro *= nums[i]
        
        return res