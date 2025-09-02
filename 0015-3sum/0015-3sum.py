class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        res = []
        nums.sort()

        i = 0
        while i < len(nums) - 2:

            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:

                if (nums[i] + nums[j] + nums[k]) == 0:
                    res.append([nums[i],nums[j],nums[k]])

                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    k -= 1

            i += 1
        return res
            


        # res = []
        # nums.sort()
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     j = i + 1
        #     k = len(nums) - 1
        #     while j < k:
        #         total = nums[i] + nums[j] + nums[k]
        #         if total > 0:
        #             k -= 1
        #         elif total < 0:
        #             j += 1
        #         else:
        #             res.append([nums[i], nums[j], nums[k]])
        #             j += 1
        #             while nums[j] == nums[j-1] and j < k:
        #                 j += 1
        # return res

        # res = []
        # nums.sort()
        # for i in range(len(nums)-2):
        #     for j in range(i+1,len(nums)-1):
        #         add = nums[i] + nums[j]
        #         ano_num = -1 * add
        #         if ano_num in nums[j+1:] and [nums[i],nums[j],ano_num] not in res:
        #             res.append([nums[i],nums[j],ano_num])

        # return res