class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = len(s)
        m = len(t)
        if l != m:
            return False
        mapdict1 = {}
        mapdict2 = {}
        for i,char in enumerate(s):
            if t[i] not in mapdict1:
                mapdict1[t[i]] = char
            if char not in mapdict2:
                mapdict2[char] = t[i]
            if mapdict2[char] != t[i]:
                return False
            if mapdict1[t[i]] != char:
                    return False

        return True