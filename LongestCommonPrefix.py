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

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))