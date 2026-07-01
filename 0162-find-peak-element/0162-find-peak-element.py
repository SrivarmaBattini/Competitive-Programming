class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        max_val = nums[0]
        max_ind = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] > max_val:
                max_val = nums[i]
                max_ind = i

        return max_ind