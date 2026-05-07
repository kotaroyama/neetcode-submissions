class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            pairs.append((position[i], speed[i], time))
        
        # Sort pairs by position
        pairs = sorted(pairs, key=lambda x: x[0], reverse=True)
        stack = []
        for pair in pairs:
            stack.append(pair)
            if len(stack) > 1:
                if stack[-1][2] <= stack[-2][2]:
                    stack.pop()           

        return len(stack)