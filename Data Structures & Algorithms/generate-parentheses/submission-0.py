class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = ""
        open_p = 0
        close_p = 0

        def helper(n, result, path, open_p, close_p):
            if close_p == n:
                result.append(path)
            
            if open_p < n:
                path = path + "("
                helper(n, result, path, open_p + 1, close_p)
                path = path[:-1]

            if open_p >= 1 and close_p < open_p:
                path = path + ")"
                helper(n, result, path, open_p, close_p + 1)
                path = path[:-1]

        helper(n, result, path, open_p, close_p)
        return result
