class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        aroundH = [-1, -1, -1, 0, 1, 1, 1, 0]
        aroundV = [-1, 0, 1, 1, 1, 0, -1, -1]

        temp = [[0] * len(board[0]) for _ in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[i])):
                temp[i][j] = board[i][j]
                dies = 0
                live = 0
                for k in range(len(aroundH)):
                    neighborH = i + aroundH[k]
                    neighborV = j + aroundV[k]
                    if neighborH < 0 or neighborH == len(board) or neighborV < 0 or neighborV == len(board[i]):
                        continue
                    if board[neighborH][neighborV] == 1:
                        live += 1
                    else:
                        dies += 1
                if board[i][j] == 1:
                    #Any live cell with fewer than two live neighbors dies as if caused by under-population.
                    #Any live cell with two or three live neighbors lives on to the next generation.
                    #Any live cell with more than three live neighbors dies, as if by over-population.
                    if live < 2 or live > 3:
                        temp[i][j] = 0
                else:
                    #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                    if live == 3:
                        temp[i][j] = 1
        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] = temp[i][j]

    def inplace(self, board: List[List[int]]) -> None:
        aroundH = [-1, -1, -1, 0, 1, 1, 1, 0]
        aroundV = [-1, 0, 1, 1, 1, 0, -1, -1]

        for i in range(len(board)):
            for j in range(len(board[i])):
                dies = 0
                live = 0
                for k in range(len(aroundH)):
                    neighborH = i + aroundH[k]
                    neighborV = j + aroundV[k]
                    if neighborH < 0 or neighborH == len(board) or neighborV < 0 or neighborV == len(board[i]):
                        continue
                    if board[neighborH][neighborV] == 1 or board[neighborH][neighborV] == -1:
                        live += 1
                    else:
                        dies += 1
                if board[i][j] == 1:
                    #Any live cell with fewer than two live neighbors dies as if caused by under-population.
                    #Any live cell with two or three live neighbors lives on to the next generation.
                    #Any live cell with more than three live neighbors dies, as if by over-population.
                    if live < 2 or live > 3:
                        board[i][j] = -1
                else:
                    #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
                    if live == 3:
                        board[i][j] = 2
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
                