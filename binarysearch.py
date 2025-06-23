# #Q1. Binary search
# class Soltuion:
#     def search(self,nums,target):
#         left, right=0,len(nums)-1
#         while left<=right:
#             mid=(left+right)//2
#             if nums[mid]==target:
#                 return mid
#             elif nums[mid]<target:
#                 left=mid+1
#             else:
#                 right=mid-1

#         return -1
# nums=[-1,0,2,4,6,8]
# target = 4
# sol=Soltuion()
# print(sol.search(nums,target))

#Q2. search a 2d matrix
# class Solution:
#     def searchMatrix(self,matrix,target):
#         if not matrix or not matrix[0]:
#             return False
#         m,n=len(matrix),len(matrix[0])
#         left,right=0,m*n-1
#         while left<=right:
#             mid=(left+right)//2
#             row,col=divmod(mid,n)
#             mid_val=matrix[row][col]
#             if mid_val==target:
#                 return True
#             elif mid_val < target:
#                 left=mid+1
#             else:
#                 right=mid-1
#         return False

# matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
# target = 10
# sol=Solution()
# print(sol.searchMatrix(matrix,target))

#Q3. Eating Bananas
# import math
# class Solution():
#     def minEatingSpeed(self,piles,h):
#         left,right=1,max(piles)
#         result=right
#         while left<=right:
#             mid=(left+right)//2
#             hours=sum(math.ceil(p/mid)for p in piles)
#             if hours<=h:
#                 result=mid
#                 right=mid-1
#             else:
#                 left=mid+1
#         return result
# piles = [1,4,3,2]
# h = 9
# sol=Solution()
# print(sol.minEatingSpeed(piles,h))

#Q4. Min in sorted array
# class Solution():
#     def findMin(self,nums):
#         left,right=0,len(nums)-1
#         while left<right:
#             mid=(left+right)//2
#             if nums[mid]>nums[right]:
#                 left=mid+1
#             else:
#                 right=mid
#         return nums[left]
    
# sol=Solution()
# nums = [3,4,5,6,1,2]
# print(sol.findMin(nums))

#Q5. search in rotated array
# class Solution():
#     def search(self,nums,target):
#         left,right=0,len(nums)-1
#         while left<=right:
#             mid=(left+right)//2
#             if nums[mid]==target:
#                 return mid
#             if nums[left]<=nums[mid]:
#                 if nums[left]<=target<nums[mid]:
#                     right=mid-1
#                 else:
#                     left=mid+1
#             else:
#                 if nums[mid]<target<=nums[right]:
#                     left=mid+1
#                 else:
#                     right=mid-1
#         return -1
# sol=Solution()
# nums=[4,5,6,7,0,1,2]
# target=0
# print(sol.search(nums,target))

#Q5. time based key value store
# from collections import defaultdict
# import bisect
# class TimeMap:

#     def __init__(self):
    #     self.store=defaultdict(list)
        

    # def set(self, key: str, value: str, timestamp: int) -> None:
    #     self.store[key].append((timestamp,value))
        

    # def get(self, key: str, timestamp: int) -> str:
    #     if key not in self.store:
    #         return ""
        
    #     values = self.store[key]
    #     left,right=0,len(values)-1
    #     result=""
    #     while left<=right:
    #         mid=(left+right)//2
    #         if values[mid][0]<=timestamp:
    #             result=values[mid][1]
    #             left=mid+1
    #         else:
    #             right=mid-1
    #     return result
        
#Q6. median of two sorted arrays
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2):
        # if len(nums1)>len(nums2):
        #     nums1,nums2=nums2,nums1
        # x,y=len(nums1),len(nums2)
        # low, high = 0, x

        # while low <= high:
        #     partitionX = (low + high) // 2
        #     partitionY = (x + y + 1) // 2 - partitionX

        #     # Edge handling: -inf for empty partition left, +inf for empty partition right
        #     maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
        #     minRightX = float('inf') if partitionX == x else nums1[partitionX]

        #     maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
        #     minRightY = float('inf') if partitionY == y else nums2[partitionY]

        #     if maxLeftX <= minRightY and maxLeftY <= minRightX:
        #         # Found correct partition
        #         if (x + y) % 2 == 0:
        #             return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
        #         else:
        #             return max(maxLeftX, maxLeftY)
        #     elif maxLeftX > minRightY:
        #         # Move towards left in nums1
        #         high = partitionX - 1
        #     else:
        #         # Move towards right in nums1
        #         low = partitionX + 1

        # raise ValueError("Input arrays are not sorted")
        