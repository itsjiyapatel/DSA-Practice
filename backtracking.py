# # def backtrack(start, path):
#     # 1. Save the current path
#     # 2. Iterate from 'start' to end
#     #     a. Include current element
#     #     b. Recurse
#     #     c. Backtrack (remove last element)
# #Q1. Subsets
# from typing import List

# class Solution:
#     def subsets(self,nums):
#         result=[]
#         def backtrack(start,subset):
#             result.append(subset[:])
#             for i in range(start,len(nums)):
#                 subset.append(nums[i])
#                 backtrack(i+1,subset)
#                 subset.pop()
#         backtrack(0,[])
#         return result
    
# sol=Solution()
# nums=[1,2,3]
# print(sol.subsets(nums))

# #Q2. Combination Sum
# class Solution:
#     def combinationSum(self,nums,target):
#         result=[]
#         def backtrack(start,path,length):
#             if length==0:
#                 result.append(path[:])
#                 return
#             if length<0:
#                 return
            
#             for i in range(start,len(nums)):
#                 path.append(nums[i])
#                 backtrack(i,path,length-nums[i])
#                 path.pop()
#         backtrack(0,[],target)
#         return result

# sol=Solution()
# nums = [3,4,5]
# target=16
# print(sol.combinationSum(nums,target))

# #Q3. Combination sum II
# class Solution:
#     def combinationSum2(self,nums,target):
#         nums.sort()
#         result=[]

#         def backtrack(start,path,length):
#             if length==0:
#                 result.append(path[:])
#                 return
#             if length<0:
#                 return 
            
#             for i in range(start,len(nums)):
#                 if i>start and nums[i]==nums[i-1]:
#                     continue

#                 path.append(nums[i])
#                 backtrack(i+1,path,length-nums[i])
#                 path.pop()
#         backtrack(0,[],target)
#         return result
    
# sol = Solution()
# candidates = [9,2,2,4,6,1,5]
# target = 8
# print(sol.combinationSum2(candidates, target))

# #Q4. Permutations
# class Solution:
#     def permute(self,nums):
#         result=[]
#         def backtrack(path,remaining):
#             if not remaining:
#                 result.append(path)
#                 return 
#             for i in range(len(remaining)):
#                 backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

#         backtrack([], nums)
#         return result
    
# sol = Solution()
# nums = [1, 2, 3]
# print(sol.permute(nums))

#Q5. Subsets 2

class Solution:
    def subsetsWithDup(self, nums):
        result = []
        nums.sort()  

        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()  # Backtrack

        backtrack(0, [])
        return result

sol = Solution()
nums = [1, 2, 1]
print(sol.subsetsWithDup(nums))
