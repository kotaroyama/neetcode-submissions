class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            print(stack)
            if (tokens[i] == "+" or
                tokens[i] == "-" or
                tokens[i] == "*" or
                tokens[i] == "/"):
                x = int(stack.pop())
                y = int(stack.pop())
                if tokens[i] == "+":
                    stack.append(x + y)
                elif tokens[i] == "-":
                    stack.append(y - x)
                elif tokens[i] == "*":
                    stack.append(x * y)
                elif tokens[i] == "/":
                    stack.append(y / x)
            else:
                stack.append(tokens[i])

        return int(stack[-1])