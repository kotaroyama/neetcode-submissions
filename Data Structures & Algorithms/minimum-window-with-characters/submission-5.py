class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        hash_map = defaultdict(int)
        for c in t:
            hash_map[c] += 1

        window = {}
        have = 0
        need = len(hash_map)
        result = [-1, -1]
        result_len = float("inf")
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in window:
                window[c] += 1
            else:
                window[c] = 1
            
            if c in hash_map and window[c] == hash_map[c]:
                have += 1

            while have == need:
                if (r - l + 1) < result_len:
                    result = [l, r]
                    result_len = r - l + 1
                window[s[l]] -= 1

                if s[l] in hash_map and window[s[l]] < hash_map[s[l]]:
                    have -= 1
                l += 1
        l, r = result
        return s[l : r + 1] if result_len != float("inf") else ""
