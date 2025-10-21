class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        m = len(s)
        n = len(t)
        freq = {}
        for char in t:
            freq[char] = freq.get(char , 0) + 1
        window_freq = {}
        req = len(freq.keys())
        formed = 0
        i,j = 0,0
        mini, minj, minl = 0,0,1000000
        while j < m:
            window_freq[s[j]] = window_freq.get(s[j] , 0) + 1

            if (s[j] in t) and window_freq[s[j]] == freq[s[j]]:
                formed += 1
            
            while formed == req:
                if (j - i) < minl:
                    minj = j + 1
                    mini = i
                    minl = j - i + 1
                if s[i] not in t:
                    window_freq[s[i]] -= 1
                    i +=1
                    continue
                if (window_freq[s[i]] - 1) >= freq[s[i]]: 
                    window_freq[s[i]] -= 1
                    i += 1
                else:
                    window_freq[s[i]] -= 1
                    formed -= 1
                    i += 1
                
            j += 1
        if minl == 1000000:
            return ""
        else:
            return s[mini : minj]
        
        