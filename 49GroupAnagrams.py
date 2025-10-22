class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramMap = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            anagramMap[key].append(s)
        return anagramMap.values()