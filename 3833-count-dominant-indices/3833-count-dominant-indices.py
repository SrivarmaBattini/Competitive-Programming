class Solution:
    def dominantIndices(self, nums: List[int]) -> int:

        total = sum(nums)
        domi = 0
        tot = total
        n = len(nums)
        
        for i in range(len(nums)     - 1):
            total -= nums[i]
            avg = total / (n - i - 1)

            if nums[i] > avg:
                domi += 1

        return domi