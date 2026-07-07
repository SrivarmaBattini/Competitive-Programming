class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # result = []
        # used = [False] * len(nums)
        
        # def backtrack(path):
            
        #     if len(nums) == len(path):
        #         result.append(path[:])
        #         return

        #     for i in range(len(nums)):
        #         if used[i]:
        #             continue
                
        #         used[i] = True
        #         path.append(nums[i])

        #         backtrack(path)

        #         path.pop()
        #         used[i] = False
        # backtrack([])
        # return result

        result = []

        def backtrack(start):
            if start == len(nums):
                result.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]
            
        backtrack(0)
        return result