class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        
        n = len(grid)
        output = []
        nums = {}

        for num_list in grid:
            for num in num_list:
                nums[num] = nums.setdefault(num, 0) + 1

                if nums[num] > 1:
                    output.append(num)
                    


        for i in range(1,(n**2)+1):
            if i not in nums:
                output.append(i)
                break

        return output  