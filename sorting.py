#Selection Sort- move min to front
class Solution:
    def selectionSort(self, nums):
        n=len(nums)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if nums[j]<nums[min_index]:
                    min_index=j
            nums[i],nums[min_index]=nums[min_index],nums[i]
        return nums

arr = [64, 25, 12, 22, 11]
sol=Solution()
print("Selection Sorted:", sol.selectionSort(arr))

#Bubble sort- compare if greater swap ie move max to back
def bubbleSort(nums):
    n=len(nums)
    for i in range(n):
        swapped=False
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
                swapped=True
        if not swapped:
            break
    return nums
nums=[13,24,19,29,9]
print("Bubble sorted: " , bubbleSort(nums))

#Insertion Sort- sort while inserting
def insertionSort(nums):
    n=len(nums)
    for i in range(1,n):
        key=nums[i]
        j=i-1
        while j>=0 and key<nums[j]:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=key
    return nums
nums = [12, 11, 13, 5, 6]
print("Insertion Sorted: ", insertionSort(nums))
