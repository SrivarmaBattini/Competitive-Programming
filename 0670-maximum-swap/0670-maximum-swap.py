class Solution:
    def maximumSwap(self, num: int) -> int:
        
        digit = []
        n = num
        while n > 0:
            digit.append(n%10)
            n = n // 10
        
        flag = True
        for i in range(len(digit)-1):
            if digit[i] > digit[i+1]:
                flag = False
                break
        
        if flag:
            return num
        else:
            max_num = int(num)
            for i in range(len(digit)-1):
                for j in range(i+1, len(digit)):
                    temp = digit[::-1]
                    temp[i], temp[j] = temp[j], temp[i]
                    value = int("".join(map(str, temp)))
                    max_num = max(max_num, value)
            return max_num