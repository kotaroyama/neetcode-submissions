class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []
        for i in range(len(operations)):
            if operations[i] == "+":
                item = results[-1] + results[-2]
                results.append(item)
            elif operations[i] == "C":
                results.pop()
            elif operations[i] == "D":
                item = results[-1] * 2
                results.append(item)
            else:
                results.append(int(operations[i]))
        
        return sum(results)