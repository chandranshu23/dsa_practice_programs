class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dct = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        # l = len(str(s))
        # ans = dct[s[0]]
        # a = s[1:]
        # for i, element in enumerate(a):
        #     if (element in ['M','D'] and s[i] == 'C') or (element in ['X','V'] and s[i] == 'I') or (element in ['C','L'] and s[i] == 'X'):
        #         ans -= dct[s[i]]
        #         ans += dct[element] - dct[s[i]]
        #     else:
        #         ans += dct[element]
        # return ans
        
        # dct = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        # ans = 0
        # l = len(s)
        # for i,element in enumerate(s):
        #     if (i+1 < l) and dct[element] < dct[s[1+i]]:
        #         ans -= dct[element]
        #     else:
        #         ans += dct[element]
        # return ans
        
        dct = {'I':1 , 'V':5 , 'X':10 , 'L':50 , 'C':100 , 'D':500 , 'M':1000}
        ans = 0
        l = len(s)
        for i in range(l):
            if i+1 < l and dct[s[i]] < dct[s[i+1]]:
                ans -= dct[s[i]]
            else:
                ans += dct[s[i]]
        return ans  
