class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1 or k == 1:
            return nums
        
        streak = 1
        res = []

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                streak += 1
            else:
                streak = 1
            
            if i >= k - 1:
                if streak >= k:
                    res.append(nums[i])
                else:
                    res.append(-1)
        return res