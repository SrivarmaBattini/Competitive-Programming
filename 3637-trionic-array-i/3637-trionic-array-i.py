class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        
        if len(nums) <= 3 or nums[1] < nums[0] or nums[-1] < nums[-2]:
            return False
        
        p = len(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i - 1]:
                continue
            elif nums[i] == nums[i - 1]:
                return False
            else:
                p = i - 1
                break
        
        if p == len(nums) or p == len(nums) - 1:
            return False

        q = len(nums)
        for j in range(p+1, len(nums)):
            if nums[j] < nums[j - 1]:
                continue
            elif nums[j] == nums[j - 1]:
                return False
            else:
                q = j - 1
                break
        
        def fun(ind):
            for num in range(ind + 1, len(nums)):
                if nums[num] <= nums[num - 1]:
                    return False
            return True
            
        return q < len(nums) - 1 and fun(q)