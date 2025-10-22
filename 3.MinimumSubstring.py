from collections import deque
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charset = deque()
        l = len(s)
        maxlen = 0
        currlen = 0
        i = 0
        while i < l:
            if s[i] not in charset:
                currlen += 1
                charset.append(s[i])
                if maxlen < currlen:
                    maxlen = currlen
            else:
                while charset[0] != s[i]:
                    b = charset.popleft()
                    currlen -= 1
                
                charset.popleft() 
                currlen -= 1

                charset.append(s[i])
                currlen += 1
            i += 1
        return maxlen