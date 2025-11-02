class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        nums.sort()
        n = max(nums)
        i = 0
        j = min(nums)
        res = []
        
        while i < len(nums):
            if nums[i] == j:
                j += 1
                i += 1
            else:
                res.append(j)
                j += 1

        return res