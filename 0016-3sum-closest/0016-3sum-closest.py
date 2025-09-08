class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        res = float('inf')
        ans = 0

        i = 0
        while i < len(nums) - 2:
            j, k = i+1, len(nums) - 1

            while j < k:

                total = nums[i] + nums[j] + nums[k]
                diff = abs(total - target)

                if diff < res:
                    ans = total
                    res = diff
                
                if total == target:
                    return total
                elif total < target:
                    j += 1
                else:
                    k -= 1
            
            i += 1
        return ans