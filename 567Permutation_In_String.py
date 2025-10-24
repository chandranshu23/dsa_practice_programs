from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l = len(s1)
        m = len(s2)
        s1_count = Counter(s1)
        s2_count = Counter(s2[:l])

        #if s1 is longer than s2, no permutation of s1 can exist in s2
        if l > m:
            return False

        #checking if the first window is a valid permutation
        if s1_count == s2_count:
            return True

        #sliding the window and finding any valid permuation of s1
        for i in range(1, m - l + 1):
            charOut = s2[i - 1]
            s2_count[charOut] -= 1
            
            #clearing the counter of any 0 freq elements
            if s2_count[charOut] == 0:
                del s2_count[charOut]
            
            #adding the next char in the window
            charIn = s2[i + l - 1]
            s2_count[charIn] = s2_count.get(charIn, 0) + 1

            #checking for valid permuatation
            if s1_count == s2_count:
                return True

        #no permutation found
        return False