class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        ans = 0
        check = set()
        check.add(0)
        i = 0
        while i >= 0 and i < len(instructions):
            if instructions[i] == "jump":
                i = i + values[i]
            else:
                ans += values[i]
                i += 1

            leng = len(check)
            check.add(i)
            if leng == len(check):
                break
            # if i in check:
            #     break
            # check.append(i)

        return ans
            
                
            