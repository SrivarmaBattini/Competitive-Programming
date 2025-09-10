class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        if len(nums) == len(set(nums)):
            return len(nums)

        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j] and i+1 != j:
                i += 1
                nums[i] = nums[j]
            elif nums[i] != nums[j] and i+1 == j:
                i += 1
            else:
                nums[j] = '_'
            j += 1

        return i+1