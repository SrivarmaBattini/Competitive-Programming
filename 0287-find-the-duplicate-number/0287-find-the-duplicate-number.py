class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        freq  = dict()
        for num in nums:
            freq[num] = freq.setdefault(num, 0) + 1
        
        for u,v in freq.items():
            if v >= 2:
                return u
        
        # nums = sorted(nums)

        # for i in range(1,len(nums)):
        #     if nums[i] ^ nums[i - 1] == 0:
        #         return nums[i]