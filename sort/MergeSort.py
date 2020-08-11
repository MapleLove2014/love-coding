from Exchanger import exchange
from Generator import randomNums
from Validator import isSorted
import time

class MergeSort():

    def sortBottomUp(self, nums):
        size = 1
        while size < len(nums):
            for i in range(0, len(nums), size + size):
                self.merge(nums, i, i + size - 1, min(i + size + size - 1, len(nums) - 1))
            size = size * 2
        return nums


    def sortRecursive(self, nums):
        self.sort(nums, 0, len(nums) - 1)
        return nums

    def sort(self, nums, start, end):
        if start >= end:
            return
        mid = (start+end) // 2
        self.sort(nums, start, mid)
        self.sort(nums, mid + 1, end)
        self.merge(nums, start, mid, end)
    

    def merge(self, nums, low, mid, high):
        aux = [ n for n in nums]

        i = low
        j = mid + 1
        k = low
        while k <= high:
            if i > mid:
                # low -> middle已经合并完毕
                nums[k] = aux[j]
                j += 1
            elif j > high:
                nums[k] = aux[i]
                i += 1
            elif nums[i] < nums[j]:
                nums[k] = aux[i]
            else:
                nums[k] = aux[j]
            k += 1

m = MergeSort()
print(isSorted(m.sortRecursive(randomNums(20))))
print(isSorted(m.sortRecursive(randomNums(20))))
print(isSorted(m.sortRecursive(randomNums(20))))
print(isSorted(m.sortRecursive(randomNums(20))))
print(isSorted(m.sortRecursive(randomNums(20))))


print(isSorted(m.sortBottomUp(randomNums(20))))
print(isSorted(m.sortBottomUp(randomNums(21))))
print(isSorted(m.sortBottomUp(randomNums(2200))))
print(isSorted(m.sortBottomUp(randomNums(23))))
print(isSorted(m.sortBottomUp(randomNums(25))))

t1 = time.time()
print(isSorted(m.sortRecursive(randomNums(2200))))
t2 = time.time()
print(isSorted(m.sortBottomUp(randomNums(2200))))
t3 = time.time()
sorted(randomNums(2200))
t4 = time.time()

print('{}  VS  {}   VS   {}'.format(t2-t1, t3-t2, t4-t3))
