class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        i = 0
        high = len(nums)-1
        low = 0
        while i <= high:
            if nums[i] == 0 and i != low:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
            elif nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
            else:
                i += 1