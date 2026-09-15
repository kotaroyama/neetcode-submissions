class Solution:
    def decodeString(self, s: str) -> str:
        result = ""
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                char_repeat = ""
                while stack and stack[-1].isdigit():
                    char_repeat += stack.pop()
                stack.append(int(char_repeat[::-1]) * substr)
        
        return "".join(stack)