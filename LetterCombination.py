class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        tree = [0] * (3 ^ n + 1)
        for i in range(len(digits)):
            start = (3 ^ (i + 1) - 1) // 2
            nodes = 3 ^ i
            a, b, c = self.getDigitChars(digits[i])
            while start < (3 ^ (i + 2) - 1) // 2:
                tree[start] = a
                tree[start + 1] = b
                tree[start + 2] = c
                start += 3
        # 广度优先遍历

        result  = []


    def travel(self, tree, digits):
        lastLevel = len(digits) - 1
        start = self.getLevelStart(lastLevel)
        memory = [0] * (3 ^ (lastLevel - 1))

        for i in range(start, len(tree))
            






    def getLevelStart(self, level):
        return (3 ^ (level + 1) - 1) // 2



    def getDigitChars(self, digit):
        start = (int(digit) - 2) * 3 + ord('a')
        return (chr(start), chr(start+1), chr(start+2))