class ZigZag:
    def convert(self, s: str, numRows: int) -> str:
        if not s or len(s) <= 2 or numRows <= 1:
            return s

        table = [['0' for _ in range(len(s))] for _ in range(numRows)]

        sIndex = 0
        innerLength = numRows - 2
        j = 0
        
        # convert
        while j < len(s):
            i = 0
            while i < numRows:
                if sIndex >= len(s):
                    break
                if j % (innerLength + 1) == 0:
                    table[i][j] = s[sIndex]
                    sIndex += 1
                    if i == numRows - 1:
                        j += 1
                    i += 1
            
                else:
                    table[numRows - 1 - j % (innerLength + 1)][j] = s[sIndex]
                    sIndex += 1
                    j += 1

            if sIndex >= len(s):
                break
        # read
        ss = []
        for i in range(numRows):
            for jj in range(len(s)):
                if table[i][jj] != '0':
                    ss.append(table[i][jj])

        return ''.join(ss)


    # 优化点：
    # 空间压缩到 O(n)
    # 时间压缩到 O(n)
    def convert2(self, s: str, numRows: int) -> str:
        if not s or len(s) <= 2 or numRows <= 1:
            return s

        table = [[] for _ in range(numRows)]

        goingDown = False
        i = 0
        for c in s:
            table[i].append(c)
            if i == 0 or i == numRows - 1:
                goingDown = not goingDown
            i += 1 if goingDown else -1

        ss = []
        for row in table:
            ss.extend(row)

        return ''.join(ss)




zigZag = ZigZag()
print(zigZag.convert('PAYPALISHIRING', 3))