class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        idx = -1
        for i in range(len(nums)):
            if nums[i] >= 0:
                idx = i
                break

        if idx == -1:
            i = len(nums) - 2
            j = len(nums) - 1
        else:
            i = idx - 1
            j = idx
        res = []

        while i >= 0 or j < len(nums):
            
            if i >= 0 and j < len(nums):
                if abs(nums[i]) > abs(nums[j]):
                    res.append(nums[j] ** 2)
                    j += 1
                else:
                    res.append(nums[i] ** 2)
                    i -= 1
            elif i >= 0 and j >= len(nums):
                res.append(nums[i] ** 2)
                i -= 1
            elif i < 0 and j < len(nums):
                res.append(nums[j] ** 2)
                j += 1
            else:
                i -= 1
                j += 1
            

        return res