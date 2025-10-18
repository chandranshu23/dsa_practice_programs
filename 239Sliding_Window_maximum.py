
# --------- This solution for the problem is correct but has a poor time complexity of O(N*K)
#---------- due to which we will have to go with a better solution
# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         l = len(nums)
#         if l == 1:
#             return [nums[0]]
#         lst = []
#         i=0
#         while i+k <= l:
#             lst.append(max(nums[i:i+k]))
#             i += 1
#         return lst

#------------ optimal approach using Monotonic Deque
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        d = deque()

        for i, num in enumerate(nums):
            while d and nums[d[-1]] <= num:
                d.pop()
            
            d.append(i)

            if d[0] == i-k:
                d.popleft()

            if i >= k-1:
                result.append(nums[d[0]])
        
        return result