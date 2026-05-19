class Solution:
    def partition(self, s: str) -> List[List[str]]:
        subsets = []
        path = []
        
        def helper(i):
            nonlocal subsets
            nonlocal path

            if i >= len(s):
                subsets.append(path.copy())
                return

            for j in range(i, len(s)):
                if check_pali(s, i, j):
                    path.append(s[i:j + 1])
                    helper(j + 1)
                    path.pop()

        def check_pali(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        helper(0)

        return subsets