class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_indices = {}
        for i, letter in enumerate(s):
            last_indices[letter] = i
        
        result = []
        seen = []
        cur_start = 0
        cur_end = 0
        size = 0
        for i in range(len(s) + 1):

            if i > cur_end or i == len(s):
                result.append(size)
                size = 0
                cur_start = i
                cur_end = i
                if i == len(s):
                    break

            letter = s[i]
            seen.append(letter)
            for seen_c in seen:
                cur_end = max(cur_end, last_indices[seen_c])
            
            size = cur_end - cur_start + 1
            

        return result
            