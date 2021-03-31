class Solution:
    def exist(self, board, word):
        if not word or len(word) == 0:
            return True
        if not board or len(board) == 0:
            return False
        
        def lookup(board, looked, word, i, j):
            if not word or len(word) == 0:
                return True
            dirs = [0, -1, 0, 1, 0]
            if looked[i][j] or board[i][j] != word[0]:
                return False
            for d in range(len(dirs) - 1):
                nexti = dirs[d] + i
                nextj = dirs[d+1] + j
                if nexti < 0 or nextj < 0 or nexti >= len(board) or nextj >= len(board[i]):
                    continue
                looked[i][j] = True
                if lookup(board, looked, word[1:], nexti, nextj):
                    return True
                looked[i][j] = False
            return len(word) == 1
        looked = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    if lookup(board, looked, word, i, j):
                        return True
        return False

s = Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(s.exist([["a","b"],["c","d"]], "abcd"))    
print(s.exist([["a"]], "a"))