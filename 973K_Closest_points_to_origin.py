import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        n = len(points)
        max_heap = []
        for i in range(n):
            
            heapq.heappush(max_heap,(-(points[i][0]**2 + points[i][1]**2),[points[i][0],points[i][1]]))
            if k < len(max_heap):
                heapq.heappop(max_heap)
        
        return [point for distance, point in max_heap]

