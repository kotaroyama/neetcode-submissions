class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets) == 1:
            return triplets[0] == target

        for triplet in triplets:
            for i in range(3):
                if triplet[i] > target[i]:
                    triplets.remove(triplet)
                    break
        
        hash_map = {
            target[0]: 0,
            target[1]: 0,
            target[2]: 0,
        }

        for triplet in triplets:
            if triplet[0] == target[0]:
                hash_map[target[0]] = 1
            if triplet[1] == target[1]:
                hash_map[target[1]] = 1
            if triplet[2] == target[2]:
                hash_map[target[2]] = 1
        
        if (hash_map[target[0]] == 1 and
            hash_map[target[1]] == 1 and
            hash_map[target[2]] == 1):
            return True
        
        return False