class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        ans = ""
        for subnet in address:
            if subnet != ".":
                ans += subnet
            else:
                ans += "[.]"
        return ans