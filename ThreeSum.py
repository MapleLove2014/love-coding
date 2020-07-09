class Solution:
    def threeSum(self, nums):
        sortedAbsNums = sorted(nums, key=abs)
        find, results = self.find(sortedAbsNums[::-1], 3, 0)
        if not find:
            return []
        return list({ str(sorted(t)): list(t) for t in results }.values())
    
    def find(self, nums, n, s):
        if len(nums) == n:
            return (True, [tuple(nums)]) if sum(nums) == s else (False, None)
        if len(nums) < n:
            return (False, None)
        if n == 1:
            result = [ (e, ) for e in nums if e == s ] 
            return (True, result) if result else (False, None)
        
        result = []
        isFoundWithFirstNumber, withResults = self.find(nums[1:], n - 1, s - nums[0])
        if isFoundWithFirstNumber:
            result.extend([ (nums[0],) + t for t in withResults])
        isFoundWithoutFirstNumber, withoutResults = self.find(nums[1:], n, s)
        if isFoundWithoutFirstNumber:
            result.extend(withoutResults)
        if not isFoundWithFirstNumber and not isFoundWithoutFirstNumber:
            return (False, None)
        return (True, result)

    def twoPointers(self, nums):
        if not nums or len(nums) < 3:
            return []
        sortedNums = sorted(nums)
        resultDict = {}
        i = 0
        for i in range(len(nums) - 2):
            if sortedNums[i] > 0:
                break
            if i > 0 and sortedNums[i - 1] == sortedNums[i]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if sum([sortedNums[i], sortedNums[j], sortedNums[k]]) == 0:
                    resultDict['{}-{}-{}'.format(sortedNums[i], sortedNums[j], sortedNums[k])] = [sortedNums[i], sortedNums[j], sortedNums[k]]
                    k -= 1
                    j += 1
                elif sum([sortedNums[i], sortedNums[j], sortedNums[k]]) > 0:
                    k -= 1
                else:
                    j += 1
        return list(resultDict.values())

    
    def hashBasedSolution(self, nums):
        sortedNums = sorted(nums)
        resultDict = {}
        for i in range(len(nums) - 2):
            if sortedNums[i] > 0:
                break
            j = i + 1
            loopDict = {}
            while j < len(nums):
                if (0 - sortedNums[i] - sortedNums[j]) in loopDict:
                    resultDict[str(sorted([sortedNums[i], sortedNums[j], 0 - sortedNums[i] - sortedNums[j]]))] = [sortedNums[i], sortedNums[j], 0 - sortedNums[i] - sortedNums[j]]
                loopDict[sortedNums[j]] = sortedNums[j]
                j += 1
        return list(resultDict.values())




s = Solution()

print(s.twoPointers([0, 0, 0]))
print(s.twoPointers([-1, 0, 1, 2, -1, -4]))

print(s.hashBasedSolution([0, 0, 0]))
print(s.hashBasedSolution([-1, 0, 1, 2, -1, -4]))

#print(s.threeSum([0, 0, 0]))
#print(s.threeSum([-1, 0, 1, 2, -1, -4]))
#print(s.threeSum([-7,-1,-13,2,13,2,12,3,-11,3,7,-15,2,-9,-13,-13,11,-10,5,-13,2,-12,0,-8,8,-1,4,10,-13,-5,-6,-4,9,-12,5,8,5,3,-4,9,13,10,10,-8,-14,4,-6,5,10,-15,-1,-3,10,-15,-4,3,-1,-15,-10,-6,-13,-9,5,11,-6,-13,-4,14,-3,8,1,-4,-5,-12,3,-11,7,13,9,2,13,-7,6,0,-15,-13,-11,-8,9,-14,1,11,-7,13,0,-6,-15,11,-6,-2,4,2,9,-15,5,-11,-11,-11,-13,5,7,7,5,-10,-7,6,-7,-11,13,9,-10,-9]))

