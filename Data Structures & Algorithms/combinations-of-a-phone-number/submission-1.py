class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        hash_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        result = []
        path = ""

        def helper(i):
            nonlocal result
            nonlocal path
            if i == len(digits):
                result.append(path)
                return

            for j in range(len(hash_map[digits[i]])):
                path = path + hash_map[digits[i]][j]
                helper(i + 1)
                path = path[:-1]

        
        helper(0)
        return result
