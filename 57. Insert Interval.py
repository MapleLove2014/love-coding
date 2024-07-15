class Solution:
    def insert(self, intervals, newInterval):
        
        intervals.append(newInterval)
        return self.merge(intervals)


    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda interval:interval[0])
        result = []
        preLeft = intervals[0][0]
        preRight = intervals[0][1]
        for interval in intervals:
            if interval[0]  <= preRight:
                preRight = max(interval[1], preRight)
                preLeft = min(interval[0], preLeft)
            else:
                result.append([preLeft, preRight])
                preLeft = interval[0]
                preRight = interval[1]
        result.append([preLeft, preRight])
        return result
    
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i=0
        while i < len(intervals) and newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
            i+=1
        # newInterval[0] <= intervals[i][1]
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        while i < len(intervals):
            result.append(intervals[i])
            i+=1
        return result




        
s = Solution()
print(s.insert([[1,3],[6,9]], [2,5]))


