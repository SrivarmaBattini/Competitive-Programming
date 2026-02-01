class Solution:
    def finalElement(self, nums: List[int]) -> int:

        # i = 0
        
        # while len(nums) > 1:
        #     if i % 2 == 0:
        #         m = max(nums)
        #         mi = nums.index(m)
        #         n = len(nums)
                
        #         if n // 2 <= mi:
        #             nums = nums[mi:]
        #         else:
        #             nums = nums[:mi + 1]
        #     else:
        #         m = min(nums)
        #         mi = nums.index(m)
        #         n = len(nums)

        #         if n // 2 <= mi:
        #             nums = nums[mi:]
        #         else:
        #             nums = nums[:mi + 1]
        #     i += 1

        # return nums[0]
        
        return max(nums[0], nums[-1])