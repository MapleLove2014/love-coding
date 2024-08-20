class Node:
    def __init__(self, isWord=False):
        self.nodes = [None] * 26
        self.isWord = isWord

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not node.nodes[idx]:
                node.nodes[idx] = Node()
            node = node.nodes[idx]
        node.isWord = True
        

    def search(self, word: str) -> bool:
        def s(node, word):
            if not node:
                return False
            if len(word) == 0:
                return node.isWord
            for i in range(len(word)):
                if word[i] == ".":
                    r = False
                    for nn in node.nodes:
                        if nn:
                            r = r or s(nn, word[i+1:])
                    return r
                idx = ord(word[i]) - ord('a')
                if not node.nodes[idx]:
                    return False
                node = node.nodes[idx]
            return node.isWord
        return s(self.root, word)
                    
                
            
        


# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad")) #; // return False
print(wordDictionary.search("bad")) #; // return True
print(wordDictionary.search(".ad")) #; // return True
print(wordDictionary.search("b..")) #; // return True
