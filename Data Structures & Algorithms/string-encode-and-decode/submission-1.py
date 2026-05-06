class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += str(len(s))
            result += "#"
            result += s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        num = ""
        new_str = ""
        while i < len(s):
            if s[i].isdigit():
                num += s[i]
                i += 1
                continue
            elif s[i] == "#":
                num = int(num)
                new_str = s[i + 1:i + 1 + num]
                result.append(new_str)
                i += num + 1
                num = ""
                new_str = ""
                continue

        return result