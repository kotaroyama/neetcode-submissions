class Solution:
    def partition(self, s: str) -> List[List[str]]:
        subsets = []
        path = []
        
        def helper(i, j):
            nonlocal subsets
            nonlocal path

            if j >= len(s):
                if j == i:
                    subsets.append(path.copy())
                return

            if check_pali(s[i:j + 1]):
                path.append(s[i:j + 1])
                helper(j + 1, j + 1)
                path.pop()

            helper(i, j + 1)

        def check_pali(s):
            return s == s[::-1]

        helper(0, 0)

        return subsets