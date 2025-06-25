#Q1. Kth largest element
from typing import List
import heapq 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        # Initialize the min-heap with the first k elements from nums
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # If the heap has k elements, replace the root (smallest in min-heap) if the new value is larger
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
        
        # Return the kth largest, which is the root of the min-heap
        return self.min_heap[0]


operations = ["KthLargest", "add", "add", "add", "add", "add"]
values = [[3, [1, 2, 3, 3]], [3], [5], [6], [7], [8]]

output = []
kth = None

for op, val in zip(operations, values):
    if op == "KthLargest":
        k, nums = val
        kth = KthLargest(k, nums)
        output.append(None)
    elif op == "add":
        output.append(kth.add(val[0]))

print(output)