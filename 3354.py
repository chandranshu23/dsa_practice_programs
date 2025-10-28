class Solution(object):
    def checkValid(self,nums,idx,length,j):
        n = list(nums)
        while 0 <= idx and length > idx:
            if n[idx] == 0:
                idx += j
            else:
                n[idx] -= 1
                j *= -1
                idx += j
        if n.count(0) == length:
            return 1
        else:
            return 0
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        length = len(nums)
        for a,b in enumerate(nums):
            if b == 0:
                temp1 = self.checkValid(nums,a,length,1)
                temp2 = self.checkValid(nums,a,length,-1)
                ans += temp1 + temp2
        return ans
        