class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        altitude = curr = 0     
        for g in gain:
            curr += g
            altitude = max(curr, altitude)
        return altitude