class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        output = -1
        for i in range(k):
            output = -heapq.heappop(nums)
        return output