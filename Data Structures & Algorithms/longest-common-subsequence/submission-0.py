class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)

        def memoization(index1, index2, len1, len2, cache):
            key = f"{index1}-{index2}"
            if index1 == len1 or index2 == len2:
                return 0
            if key in cache:
                return cache[key]

            if text1[index1] == text2[index2]:
                print(key)
                cache[key] = 1 + memoization(index1 + 1, index2 + 1, len1, len2, cache)
            else:
                cache[key] = max(memoization(index1 + 1, index2, len1, len2, cache),
                              memoization(index1, index2 + 1, len1, len2, cache))
            return cache[key]
        
        memo = {}
        return memoization(0, 0, len1, len2, memo)

            