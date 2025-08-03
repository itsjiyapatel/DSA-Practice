# #Find min difference between max and min
# def find_min(arr,k):
#     n=len(arr)
#     arr.sort()
#     minDiff=float('inf')
#     for i in range(n-k+1):
#         diff=arr[i+k-1]-arr[i]
#         if diff<minDiff:
#             minDiff=diff
#     return minDiff

# if __name__ == "__main__":
#     arr = [7, 3, 2, 4, 9, 12, 56]
#     m = 3

#     print(find_min(arr, m))

# #heap sort
# def heapify(arr, n, i):
    
#     largest = i 
#     l = 2 * i + 1 
#     r = 2 * i + 2  
#     if l < n and arr[l] > arr[largest]:
#         largest = l

#     if r < n and arr[r] > arr[largest]:
#         largest = r

#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]  # Swap

#         heapify(arr, n, largest)

# def heapSort(arr):
    
#     n = len(arr) 

#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)

#     for i in range(n - 1, 0, -1):
      
#         arr[0], arr[i] = arr[i], arr[0] 
#         heapify(arr, i, 0)

# def printArray(arr):
#     for i in arr:
#         print(i, end=" ")
#     print()

# arr = [9, 4, 3, 8, 10, 2, 5] 
# heapSort(arr)
# print("Sorted array is ")
# printArray(arr)

# #k largest
# import heapq

# def kLargest(arr, k):

#     minH = arr[:k]
#     heapq.heapify(minH)
    
#     for x in arr[k:]:
#         if x > minH[0]:
#             heapq.heapreplace(minH, x)
    
#     res = []

#     while minH:
#         res.append(heapq.heappop(minH))

#     res.reverse()
#     return res

# if __name__ == "__main__":
#     arr = [1, 23, 12, 9, 30, 2, 50]
#     k = 3
#     res = kLargest(arr, k)
#     print(" ".join(map(str, res)))

# #Next Greater Element
# def nextLargerElement(arr):
#     n = len(arr)
#     res = [-1] * n  
#     stk = []  

#     for i in range(n - 1, -1, -1):
#         while stk and arr[stk[-1]] <= arr[i]:
#             stk.pop()

#         if stk:
#             res[i] = arr[stk[-1]]
#         stk.append(i)

#     return res

# if __name__ == "__main__":
  
#     arr = [6, 8, 0, 1, 3]
#     res = nextLargerElement(arr)
#     print(" ".join(map(str, res)))

# #kth smallest
# import heapq
# def kthSmallest(arr, K):
#     max_heap = []
#     for num in arr:
#         heapq.heappush(max_heap, -num)
#         if len(max_heap) > K:
#             heapq.heappop(max_heap)

#     return -max_heap[0]

# if __name__ == "__main__":
#     arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
#     K = 4
#     print("Kth Smallest Element is:", kthSmallest(arr, K))

#kth smallest pairs
import heapq
def kSmallestPair(nums1,nums2,k):
    if not nums1 or not nums2 or k==0:
        return []
    heap=[]
    res=[]
    for i in range(min(k,len(nums1))):
        heapq.heappush(heap,(nums1[i]+nums2[0],i,0))
        while heap and len(res)<k:
            total, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
    return res

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
print(kSmallestPair(nums1,nums2,k))