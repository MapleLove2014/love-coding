class TreeNode:
    def __init__(self, isWord = False):
        self.nodes = [None] * 26
        self.isWord = isWord

class Trie:

    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            no = ord(c) - ord('a')
            if not node.nodes[no]:
                node.nodes[no] = TreeNode()
            node =node.nodes[no]
        node.isWord = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            no = ord(c) - ord('a')
            if not node.nodes[no]:
                return False
            node = node.nodes[no]
        return node.isWord
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            no = ord(c) - ord('a')
            if not node.nodes[no]:
                return False
            node = node.nodes[no]
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
print(obj.search("wor"))
print(obj.startsWith("wor"))