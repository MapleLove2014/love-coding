class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        inverse = [[] for _ in range(numCourses)]
        degree = [0] * numCourses
        for p in prerequisites:
            sec = p[0]
            first = p[1]
            inverse[first].append(sec)
            degree[sec] += 1
        stack = []
        result = []
        for i in range(numCourses):
            if degree[i] == 0:
                stack.append(i)
        while stack:
            c = stack.pop()
            result.append(c)
            for cc in inverse[c]:
                degree[cc] -= 1
                if degree[cc] == 0:
                    stack.append(cc)
        
        return result if len(result) == numCourses else []
    
s = Solution()
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(s.findOrder(2, [[1,0]]))
print(s.findOrder(1, []))