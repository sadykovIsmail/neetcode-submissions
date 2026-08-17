class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)  == 0:
            return [[]]
        hashmap = dict()
        for w in strs:
            word = "".join(sorted(w))
            if word in hashmap:
                hashmap[word].append(w)
            else:
                hashmap[word] = [w]
        return list(hashmap.values())
