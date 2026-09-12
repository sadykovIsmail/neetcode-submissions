import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        result = []
        heap = []
        for num, times in count.items():
            heapq.heappush(heap, (-times, num))
            
        while k:
            times, num = heapq.heappop(heap)
            result.append(num)
            
            k -= 1
        return result