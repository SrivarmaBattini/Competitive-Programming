class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        nums.sort()
        n = nums[-1]
        i = 0
        j = nums[0]
        res = []
        
        while i < len(nums):
            if nums[i] == j:
                j += 1
                i += 1
            else:
                res.append(j)
                j += 1

        return res