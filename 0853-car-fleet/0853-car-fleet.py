class Solution:
    def carFleet(self, target: int, position: List[float], speed: List[float]) -> int:

        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in pairs:
            t = (target-pos) / spd
            if not stack or t > stack[-1]:
                stack.append(t)
        
        return len(stack)