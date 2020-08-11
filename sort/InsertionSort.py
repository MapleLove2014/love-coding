from Exchanger import exchange
from Generator import randomNums
from Validator import isSorted


class InsertionSort():
    # 这个也是冒泡排序
    def exchangedSort(self, nums):

        for i in range(len(nums) - 1):
            j = i + 1
            while j > 0 and nums[j - 1] > nums[j]:
                exchange(nums, j-1, j)
                j -= 1
        return nums
    
    def directSort(self, nums):
        for i in range(1, len(nums)):
            j = i - 1
            number = nums[i]
            while j >= 0 and nums[j] > number:
                nums[j + 1] = nums[j]
                j -= 1 
            if j < i - 1:
                nums[j + 1] = number
        return nums


i = InsertionSort()

print(isSorted(i.exchangedSort(randomNums(20))))
print(isSorted(i.exchangedSort(randomNums(20))))
print(isSorted(i.exchangedSort(randomNums(20))))
print(isSorted(i.exchangedSort(randomNums(20))))
print(isSorted(i.exchangedSort(randomNums(20))))

print(isSorted(i.directSort(randomNums(20))))
print(isSorted(i.directSort(randomNums(20))))
print(isSorted(i.directSort(randomNums(20))))
print(isSorted(i.directSort(randomNums(20))))
print(isSorted(i.directSort(randomNums(20))))
print(isSorted(i.directSort(randomNums(20))))





