class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        # def binary(n):
        #     s = n[::-1]
        #     val = 0
        #     for i in range(len(n)):
        #         val += int(s[i]) * (2 ** i)
        #     return val

        # value = set()
        # for num in nums:
        #     value.add(binary(num))
        # print(value)
        # i = len(nums)
        # for num in range(1, (2 ** i)):
        #     if num not in value:
        #         ans = ""
        #         while num > 0:
        #             ans = str(num%2) + ans
        #             num = num // 2
                
        #         diff = len(nums) - len(ans)
        #         pref = "0" * diff  
        #         return pref + ans
        
        # return "0" if nums[0] == "1" else "1"

        val = ""
        for i in range(len(nums)):
            if nums[i][i] == "0":
                val += "1"
            else:
                val += "0"
        
        return val