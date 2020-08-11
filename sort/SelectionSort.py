from Generator import Generator
from Validator import isSorted

class SelectionSort():

    def sort(self, nums):

        for i in range(len(nums)):
            idx = i
            for j in range(i, len(nums)):
                if nums[j] < nums[idx]:
                   idx = j
            self.exchange(nums, i, idx)
        
        return nums
            

    def exchange(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


s = SelectionSort()
g = Generator()
print(isSorted(s.sort(g.randomNums(20))))
print(isSorted(s.sort(g.randomNums(20))))
print(isSorted(s.sort(g.randomNums(20))))
print(isSorted(s.sort(g.randomNums(20))))
print(isSorted(s.sort(g.randomNums(20))))
print(isSorted(s.sort(g.randomNums(20))))

