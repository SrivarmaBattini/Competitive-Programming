class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:

        i = 1
        n = len(nums)

        while i < n:
            if nums[i] == nums[i - 1]:
                nums[i - 1] = nums[i - 1] + nums[i]
                nums.pop(i)
                n -= 1
                if i != 1:
                    i -= 1
            else:
                i += 1
        return nums[:n]