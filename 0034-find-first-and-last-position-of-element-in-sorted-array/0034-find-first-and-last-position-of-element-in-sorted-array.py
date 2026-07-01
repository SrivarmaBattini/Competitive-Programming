class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        k = -1
        for i in range(len(nums)):
            if nums[i] == target and k == -1:
                if len(res) == 0:
                    res.append(i)
                    k = i
            
            if k != -1 and res[0] != i and nums[i] == target:
                k = i
        
            if len(nums)-1 == i:
                if len(res) == 1:
                    res.append(k)
                else:
                    res = [-1,-1]
        return res if len(res) == 2 else [-1, -1]
