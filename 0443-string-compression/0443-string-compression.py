class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = j = 0

        while j < len(chars):
            char = chars[j]
            k = 0 

            while j < len(chars) and chars[j] == char:
                j += 1
                k += 1
            
            chars[i] = char
            i += 1
            if k > 1:
                for num in str(k):
                    chars[i] = num
                    i += 1 
    
        return i 