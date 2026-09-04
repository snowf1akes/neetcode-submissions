import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for key, val in count.items():
            if len(heap) < k: #number of items is less than k, just push it all onto the heap since it fits. 
                heapq.heappush(heap, (val, key))
            else:
                #heap is as large as k things
                if len(heap) == k:
                    heapq.heappushpop(heap, (val, key))
            
        return [h[1] for h in heap]

        