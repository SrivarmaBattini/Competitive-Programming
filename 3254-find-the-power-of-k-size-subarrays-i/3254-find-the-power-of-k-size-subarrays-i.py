class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1 or k == 1:
            return nums
        
        res = []
        for i in range(len(nums) - k + 1):
            flag = False
            for j in range(i + 1, i + k):
                if nums[j] != nums[j - 1] + 1:
                    res.append(-1)
                    flag = False
                    break
                else:
                    flag = True
            if flag:
                res.append(nums[i + k - 1])

        return res            