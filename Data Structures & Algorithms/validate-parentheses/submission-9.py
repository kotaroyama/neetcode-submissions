class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2:
            return False

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' or c == '}' or c == ']':
                if stack:
                    popped = stack.pop()
                    if c == ')' and popped != '(':
                        return False
                    if c == '}' and popped != '{':
                        return False
                    if c == ']' and popped != '[':
                        return False
                else:
                    return False
        if stack:
            return False

        return True