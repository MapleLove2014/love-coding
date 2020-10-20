# 一个数组上有m个点，编号为0~m-1，从0点出发，每步可以右移到下一个点，也可以左移到前一个点。
# 求：经过n步又回到0点有多少种不同的走法
# 输入步数 n 数组长度 m
# // 测试数据：
# // m=5, n=0, step=1
# // m=5, n=1, step=0
# // m=5, n=2, step=1
# // m=5, n=3, step=0
# // m=5, n=4, step=2
# // m=5, n=5, step=0
# // m=5, n=6, step=5


def solve(n, m):
    table = [[0] * m for i in range(n+1)]
    table[0][0] = 1
    for i in range(1, n+1):
        for j in range(m):
            if j == 0:
                table[i][j] = table[i-1][j+1]
            elif j == m-1:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = table[i-1][j+1] + table[i-1][j-1]
    return table[n][0]



print(solve(0, 5) == 1)
print(solve(1, 5) == 0)
print(solve(2, 5) == 1)
print(solve(3, 5) == 0)
print(solve(4, 5) == 2)
print(solve(5, 5) == 0)
print(solve(6, 5) == 5)



