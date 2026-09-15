class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        j = 0

        while i < len(chars):
            chars[j] = chars[i]
            j += 1
            k = i + 1
            while k < len(chars) and chars[i] == chars[k]:
                k += 1
            
            if k - i > 1:
                for c in str(k - i):
                    chars[j] = c
                    j += 1
            
            i = k
        return j