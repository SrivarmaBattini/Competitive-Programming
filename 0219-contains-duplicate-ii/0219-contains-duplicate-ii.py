class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        freq = dict()
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]].append(i)
            else:
                freq[nums[i]] = [i]
        
        for v in freq.values():
            if len(v) == 1:
                continue
            else:
                n = len(v)
                for i in range(1,n):
                    if v[i] - v[i-1] <= k:
                        return True
        return False