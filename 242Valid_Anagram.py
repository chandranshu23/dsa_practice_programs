class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = len(s)
        m = len(t)
        if l != m:
            return False
        freqS = {}
        freqT = {}
        i = 0 
        while i < l:
            freqS[s[i]] = freqS.get(s[i], 0) + 1
            freqT[t[i]] = freqT.get(t[i], 0) + 1
            i += 1
        
        # b = freqS.keys()
        # c = set(freqT.keys())

        # for i in b:
        #     if i not in c:
        #         return False 
        #     if freqS[i] != freqT[i]:
        #         return False
        # return True
        return freqS == freqT
