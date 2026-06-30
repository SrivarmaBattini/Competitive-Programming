class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)
        water = 0

        i = 0
        while i<n-1:
            j = i+1
            while j < n and height[i] > height[j]:
                j += 1
            
            if j == n:
                break
            
            for k in range(i+1, j):
                water += min(height[i], height[j]) - height[k]
            
            i = j
        
        r = n-1
        while r>i:
            l = r-1
            while  l >= i and height[l] < height[r]:
                l -= 1
            
            if l < i:
                break
            
            for k in range(l+1, r):
                water += min(height[l], height[r]) - height[k]
            
            r = l
        return water