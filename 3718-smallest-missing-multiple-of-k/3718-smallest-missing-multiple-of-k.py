class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        
        mini = min(nums)
        maxi = max(nums)
        maxi = maxi // k

        if mini == 0:
            mini = 1
        
        for i in range(1, maxi + 1):
            if i * k not in nums:
                return i * k
        
        return (maxi+1) * k