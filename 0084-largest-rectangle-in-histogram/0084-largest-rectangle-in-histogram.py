class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        stack = []
        max_area = 0

        for i in range(len(heights)+1):
            curr_h = heights[i] if i < len(heights) else 0

            while stack and heights[stack[-1]] > curr_h:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area