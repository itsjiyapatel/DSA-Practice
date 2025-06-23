# Q1. has duplicate
def has_duplicate(arr):
    arr.sort()
    n=len(arr)
    for i in range(n):
        if arr[i]==arr[i+1]:
            return True
        return False
    
arr1=[1,2,3,4]
arr2=[3,3,4,5]
res1=has_duplicate(arr1)
res2=has_duplicate(arr2)
print(res1, res2)

#Q2. anagrams of each other
def is_anagram(s,t):
    if len(s)!=len(t):
        return False
    
    return sorted(s)==sorted(t)

print(is_anagram("racecar","carrace"))

#Q3. two sum
def two_sum(arr,target):
    num_map={}
    for i,num in enumerate(arr):
        complement=target-num
        if complement in num_map:
            return[num_map[complement],i]
        num_map[num]=i
    return []

arr = [2, 7, 11, 15]
target = 18
print(two_sum(arr, target))

#Q4. top k frequent elements
import heapq
from collections import Counter

class Solution: 
    def topK(self, nums, k):
        freq_map=Counter(nums)
        heap=[(-freq,num) for num,freq in freq_map.items()]
        heapq.heapify(heap)
        result=[heapq.heappop(heap)[1] for _ in range(k)]
        return result

sol=Solution()
nums=[1,2,2,3,3,3]
print(sol.topK(nums,2))

#Q5. encode and decode
class Code:
    def encoder(self, str):
        return ''.join(f"{len(s)}#{s}" for s in str)
    def decoder(self,s):
        result=[]
        i=0
        while i<len(s):
            j=s.find('#',i)
            length=int(s[i:j])
            i=j+1
            result.append(s[i:i + length])
            i+=length
        return result
    
code=Code()
original=["neet","code","love","you"]
encoded=code.encoder(original)
print("Encoded: ", encoded)
decoded=code.decoder(encoded)
print("Decoded: ", decoded)

#Q6.Products of Array Except Self

class Solution:
    def productExceptSelf(self, nums):
        n=len(nums)
        output=[1]*n

        left=1
        for i in range(n):
            output[i]=left
            left=left*nums[i]
        
        right=1
        for i in range(n-1,-1,-1):
            output[i]*=right
            right=right*nums[i]

        return output
    
sol=Solution()
nums=[1,2,4,6]
print(sol.productExceptSelf(nums))

#Q7. Longest Consecutive Sequence
class Solution:
    def longestConsecutiveSeq(self,nums):
        num_set=set(nums)
        longest=0

        for num in num_set:
            if num-1 not in num_set:
                current_num=num
                current_streak=1

                while current_num+1 in num_set:
                    current_num+=1
                    current_streak+=1
                
                longest=max(longest,current_streak)

        return longest
    
sol=Solution()
nums = [0,3,2,5,4,6,1,1]
seq=sol.longestConsecutiveSeq(nums)
print(seq)

#Q8. Group Anagrams
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)

        for word in strs:
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())
 
sol=Solution()
strs = ["act","pots","tops","cat","stop","hat"]
print(sol.groupAnagrams(strs))