from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        ans = []
        len_s = len(s)
        len_p = len(p)
        
        if len_s < len_p:
            return ans
        
        p_count = Counter(p)
        s_count = Counter(s[:len_p])
        
        if s_count == p_count:
            ans.append(0)
            
        for i in range(1, len_s - len_p + 1):
            char_out = s[i - 1]
            s_count[char_out] -= 1

            if s_count[char_out] == 0:
                del s_count[char_out]
            
            char_in = s[i + len_p - 1]
            s_count[char_in] = s_count.get(char_in, 0) + 1
            
            if s_count == p_count:
                ans.append(i)
                
        return ans