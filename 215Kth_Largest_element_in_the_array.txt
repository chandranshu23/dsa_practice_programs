from heapq import heappush,heappop, heapify
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        min_heap = []
        heapify(min_heap)

        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap, num)
            elif num > min_heap[0]:
                heappop(min_heap)
                heappush(min_heap, num)

        return min_heap[0]