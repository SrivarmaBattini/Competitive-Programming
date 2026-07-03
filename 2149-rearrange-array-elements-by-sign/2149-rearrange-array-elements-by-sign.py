class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []

        for num in nums:
            if num >= 0:
                pos.append(num)
            else:
                neg.append(num)
        
        
        i = 0
        j = 0
        for k in range(len(nums)):
            if k % 2 == 0:
                nums[k] = pos[i]
                i += 1
            else:
                nums[k] = neg[j]
                j += 1
        return nums