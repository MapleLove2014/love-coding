import random

class Generator():
    def randomNums(self, length):
        nums = []
        for i in range(length):
            nums.append(random.randint(1, 100))
        return nums