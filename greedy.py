# #Activity selection
# def activitySelection(start,finish):
#     arr = list(zip(start, finish))
#     arr.sort(key=lambda x: x[1])
#     count=1
#     j=0
#     for i in range(1,len(arr)):
#         if arr[i][0]>=arr[j][1]:
#             count+=1
#             j=i
#     return count

# if __name__ == '__main__':
#     start=[1, 3, 0, 5, 8, 5]
#     finish = [2, 4, 6, 7, 9, 9]
#     print(activitySelection(start, finish))

# #Number of Coins
# def findMin(n,denomination):
#     count=0
#     for i in range(len(denomination) - 1, -1, -1):
#         while n>=denomination[i]:
#             n-=denomination[i]
#             count+=1
#     return count
# if __name__ == '__main__':
#     denomination = [1, 2, 5, 10]
#     n = 39
#     print(findMin(n, denomination))

# #min sum
# import heapq
# def minSum(arr):
#     heapq.heapify(arr)
#     num1,num2=[],[]
#     while arr:
#         num1.append(str(heapq.heappop(arr)))
#         if arr:
#             num2.append(str(heapq.heappop(arr)))

#     return int("".join(num1)) + int("".join(num2))

# arr = [5, 3, 0, 7, 4]
# print(minSum(arr))

# #min sum of two different arrays
# def findMinSum(a, b, n):

#     a.sort()
#     b.sort()
#     sum = 0
    
#     for i in range(n):
#         sum = sum + abs(a[i] - b[i])

#     return sum

# a = [4, 1, 8, 7]
# b = [2, 3, 6, 5]
# n = len(a)

# print(findMinSum(a, b, n))

