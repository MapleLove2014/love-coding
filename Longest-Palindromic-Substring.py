class DPSolution:

    def solution(self, s: str) -> str:
        table = [[-1 for _ in range(len(s))] for _ in range(len(s))]
        maxPDString = ''
        for i in range(len(s)):
            for j in range(len(s)):
                if i > j:
                    continue
                self.p(s, table, i, j)
                if table[i][j] and j - i + 1 > len(maxPDString):
                    maxPDString = s[i:j+1]
        return maxPDString

    def p(self, s, table, i, j):
        if table[i][j] != -1:
            return table[i][j]
        if i == j:
            table[i][j] = True
        elif j == i + 1:
            table[i][j] = s[i] == s[j]
        else:
            table[i][j] = self.p(s, table, i+1, j-1) and s[i] == s[j]
        return table[i][j]

    def centerAround(self, s):
        if not s or len(s) == 0:
            return ''
        start = 0
        end = 0
        for i in range(len(s)):
            len1, axes1 = self.expand(s, i, i)
            len2, axes2 = self.expand(s, i, i + 1)
            maxLen = max(len1, len2)
            if maxLen > end - start + 1:
                axes = axes1 if len1 > len2 else axes2
                start = axes[0]
                end = axes[1]
        return s[start:end+1]


    def expand(self, s, i, j):
        if i < 0 or j >= len(s) or s[i] != s[j]:
            return 0, None
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        i += 1
        j -= 1
        return j - i + 1, [i, j]





d = DPSolution()
print(d.centerAround('babd'))
print(d.solution('babd'))

