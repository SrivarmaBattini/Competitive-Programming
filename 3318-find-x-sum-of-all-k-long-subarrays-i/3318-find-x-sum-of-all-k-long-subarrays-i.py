from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        def x_sum(arr):
            
            freq = Counter(arr)
            sorted_items = sorted(freq.items(), key = lambda a: (-a[1], -a[0]))
            top_x = set(num for num, _ in sorted_items[:x])

            return sum(num for num in arr if num in top_x)


        n = len(nums)
        result = []

        for i in range(n - k + 1):
            window = nums[i: i+k]
            result.append(x_sum(window))

        return result