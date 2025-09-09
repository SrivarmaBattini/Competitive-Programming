class Solution:
    def isHappy(self, n: int) -> bool:
        ans = [n]
        flag = True

        while flag:
            num = 0
            while n != 0:
                num += ((n % 10) ** 2)
                n = n//10

            if num == 1:
                flag = False
                break
            n = num
            
            if n in ans:
                break
            else:
                ans.append(n)
        
        return not flag