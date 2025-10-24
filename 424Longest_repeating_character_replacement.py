class Solution(object):
    def characterReplacement(self, s, k):
        i = 0               
        max_len = 0         
        max_freq = 0        
        freq = {}           

        for j in range(len(s)):
            char = s[j]
            freq[char] = freq.get(char, 0) + 1
            
            max_freq = max(max_freq, freq[char])

            window_len = j - i + 1

            if window_len - max_freq > k:
                freq[s[i]] -= 1
                i += 1 
            max_len = max(max_len, j - i + 1)
            
        return max_len