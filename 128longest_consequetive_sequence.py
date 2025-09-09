class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        numSet = set(nums)
        maxSeq = 0
        current_len = 0

        for i in numSet:
            if (i-1) not in numSet:
                current_num = i
                current_len = 1
                while i+1 in numSet:
                    i += 1
                    current_len += 1
                maxSeq = max(current_len,maxSeq)
        return maxSeq

        