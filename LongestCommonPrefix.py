class Node:
    def __init__(self, parent, char):
        self.parent = parent
        self.char = char
        self.children = []
        self.keys = {}
        self.count = 0

    def hasSingleChild(self):
        return self.count == 1

    def containChild(self, char):
        return char in self.keys
    
    def addChild(self, child):
        if child.char not in self.keys:
            self.children.append(child)
            self.keys[child.char] = child
            # optimize
            self.count += 1

    def getChild(self, char):
        return self.keys[char]
        
    def getSingleChild(self):
        return self.children[0]


    def increaseChild(self):
        self.count += 1
        
    def hasChild(self):
        return self.count > 0

    def hasNoChild(self):
        return not self.hasChild()
        

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        tree = self.build(strs)
        if not tree or not tree .hasSingleChild():
            return ''
        result = []
        while tree.hasSingleChild():
            node = tree.getSingleChild()
            if node.char == '$':
                break
            result.append(node.char)
            tree = node
        return ''.join(result)


    def build(self, strs):
        if not strs or len(strs) == 0:
            return None
        root = Node(None, 'root')
        for i in range(len(strs)):
            if not strs[i]:
                return None
            self.buildTree(root, strs[i] + '${}'.format(i))
        return root

    def buildTree(self, root, string, index = 0):
        if not string or index == len(string):
            return

        if root.hasNoChild():
            node = Node(root, string[index])
            root.addChild(node)
            self.buildTree(node, string ,index + 1)
        elif root.containChild(string[index]):
            self.buildTree(root.getChild(string[index]), string, index + 1)
        else:
            root.increaseChild()


# s = Solution()
# print(s.longestCommonPrefix(["flower","flow","flight"]))
# print(s.longestCommonPrefix(["dog","racecar","car"]))

class OtherSolution:
        
    def verticalScan(self, strs) -> str:
        result = []
        i = 0
        while True:
            char = None
            for string in strs:
                if i == len(string):
                    return ''.join(result)
                if not char:
                    char = string[i]
                elif char != string[i]:
                    return ''.join(result)
                
            result.append(char)
            i += 1

    def commonPrefix(self, str1, str2):
        if not str1 or not str2:
            return ''
        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                return str1[:i]
        return str1 if len(str1) <= len(str2) else str2


    def horizontalScan(self, strs) -> str:
        if not strs:
            return ''

        prefix = strs[0]
        for i in range(1, len(strs), 1):
            if prefix == '':
                return ''
            prefix = self.commonPrefix(prefix, strs[i])
        return ''.join(prefix)
    
    def divideAndConquer(self, strs) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        return self.commonPrefix( self.divideAndConquer(strs[:len(strs) // 2]), self.divideAndConquer(strs[len(strs)//2:]) )

    def binarySearchLCP(self, strs) -> str:
        if not strs:
            return ''
        sortedStrs = sorted(strs, key=len)
        prefix = sortedStrs[0]
        hasPrefix, index = self.search(sortedStrs[0], strs, 0, len(prefix) - 1)
        return prefix[:index+1] if hasPrefix else ''


    def search(self, prefix, strs, start, end):
        if start > end:
            return (False, None)
        if start == end:
            for string in strs:
                if prefix[start] != string[start]:
                    return (False, start - 1)
            return (True, start)

        leftContain, leftIndex = self.search(prefix, strs, start, (start + end) // 2)
        if leftContain:
            rightContain, rightIndex = self.search(prefix, strs, (start + end) // 2 + 1, end)
            if rightContain:
                return (True, rightIndex)
            else:
                return (True, leftIndex)
        else:
            return (False, None)


            
o = OtherSolution()
print(o.horizontalScan(["flower","flow","flight"]))
print(o.horizontalScan(["aa","a"]))

print(o.verticalScan(["flower","flow","flight"]))
print(o.verticalScan(["dog","racecar","car"]))

print(o.divideAndConquer(["flower","flow","flight"]))
print(o.divideAndConquer(["dog","racecar","car"]))
print(o.divideAndConquer(["aa","a"]))

print(o.binarySearchLCP(["flower","flow","flight"]))
print(o.binarySearchLCP(["dog","racecar","car"]))
print(o.binarySearchLCP(["aa","a"]))
print(o.binarySearchLCP(["abcc","abcc","abcb"]))
