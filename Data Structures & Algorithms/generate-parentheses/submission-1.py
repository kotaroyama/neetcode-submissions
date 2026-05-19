class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = ""

        def helper(open_p, close_p):
            nonlocal result
            nonlocal path
            if close_p == n:
                result.append(path)
            
            if open_p < n:
                path = path + "("
                helper(open_p + 1, close_p)
                path = path[:-1]

            if open_p >= 1 and close_p < open_p:
                path = path + ")"
                helper(open_p, close_p + 1)
                path = path[:-1]

        helper(0, 0)
        return result
