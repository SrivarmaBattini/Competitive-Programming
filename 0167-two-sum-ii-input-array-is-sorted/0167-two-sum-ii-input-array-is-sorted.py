class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        ans = []
        i, j = 0, len(numbers) - 1

        while i < j:
            
            if i > 0 and numbers[i-1] == numbers[i]:
                i += 1

            total = numbers[i] + numbers[j]

            if total == target:
                ans.append(i+1)
                ans.append(j+1)
                break
            
            if total < target:
                i += 1
            else:
                j -= 1

        return ans