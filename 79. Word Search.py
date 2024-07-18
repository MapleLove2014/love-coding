class Solution:
    def exist(self, board, word: str) -> bool:
        def search(board, i, j, path, word):
            if not word:
                return True
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or path[i][j]:
                return False
            if board[i][j] != word[0]:
                return False
            d=[[0, 1], [0, -1], [-1, 0], [1, 0]]
            path[i][j] = True
            for dd in d:
                if search(board, i + dd[0], j + dd[1], path, word[1:]):
                    return True
            path[i][j] = False
            return False
        path = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(board, i, j, path, word):
                    return True
        return False
    
s = Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

print(s.exist([["S","F","C","S"],["A","D","E","E"]], "SEE"))

