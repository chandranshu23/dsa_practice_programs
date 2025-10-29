class Solution(object):
    def is_palindrome(self,sub_s):
        """Checks if a given string is a palindrome."""
        return sub_s == sub_s[::-1]

    def backtrack(self, s, start_index):
        if start_index == len(s):
            self.result.append(list(self.path))
            return

        for end_index in range(start_index, len(s)):
            substring = s[start_index : end_index + 1]
            if self.is_palindrome(substring):
                self.path.append(substring)
                self.backtrack(s, end_index + 1)
                self.path.pop()
        
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.result = []  
        self.path = []    
        
        self.backtrack(s, 0)
        return self.result

            
        

