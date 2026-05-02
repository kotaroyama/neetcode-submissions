class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_hashes = []
        for text in strs:
            char_hashes.append(self.char_hash(text))
        
        result = []
        checked = []
        for i in range(len(strs)):
            if char_hashes[i] not in checked:
               sublist = []
               sublist.append(strs[i])
               result.append(sublist)
               checked.append(char_hashes[i])
            else:
                for sublist in result:
                    if self.char_hash(sublist[0]) == self.char_hash(strs[i]):
                        sublist.append(strs[i])
        
        return result
    
    def char_hash(self, text: str):
        char_hash = {}
        for char in text:
            if char not in char_hash:
                char_hash[char] = 1
            else:
                char_hash[char] += 1
        return char_hash