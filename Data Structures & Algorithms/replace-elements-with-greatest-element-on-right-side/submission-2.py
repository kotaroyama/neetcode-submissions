class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            if i < len(arr) - 1:
                value = max(arr[i + 1:])
                result.append(value)
            else:
                result.append(-1)
        
        return result