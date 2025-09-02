class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        res = 0
        i, j = 0, len(height) - 1

        while i < j:
            length = min(height[i],height[j])
            width = j - i
            volume = length * width
            res = max(res, volume)

            if length == height[i]:
                i += 1
            else:
                j -= 1
        return res