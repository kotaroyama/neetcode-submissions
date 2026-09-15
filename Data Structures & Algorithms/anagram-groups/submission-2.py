class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        indices = {}
        for i, s in enumerate(strs):
            index = "".join(sorted(s))
            if index not in indices:
                indices[index] = []
            indices[index].append(s)
        
        result = []
        for index in indices:
            result.append(indices[index])
        return result
