class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # (index, temp)

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index, stemp = stack.pop()
                result[index] = i - index
            stack.append((i, temp))
        return result
