
# 1.预处理neighbours
neighbours = [[[] for _ in range(30)] for _ in range(30)]
delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
for r in range(30):
    for c in range(30):
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 30 and 0 <= nc < 30:
                neighbours[r][c].append((nr, nc))

# 2.遍历每个节点: 获得五十轮后的每个位置概率 -> 累乘(1 - pij)到对应的位置
empty_prob = [[1.0] * 30 for _ in range(30)]
for r in range(30):
    for c in range(30):
        dp = [[0.0] * 30 for _ in range(30)]
        dp[r][c] = 1.0
        # 获得五十轮后的每个位置概率 
        for _ in range(50): # 50轮dp迭代
            new_dp = [[0.0] * 30 for _ in range(30)]
            for i in range(30):
                for j in range(30):
                    if dp[i][j] > 0: # 概率扩散
                        each_prob = dp[i][j] / len(neighbours[i][j])
                        for x, y in neighbours[i][j]:
                            new_dp[x][y] += each_prob
            dp = new_dp
        # 累乘(1 - pij)到对应的位置
        for i in range(30):
            for j in range(30):
                empty_prob[i][j] *= (1 - dp[i][j])

# 3.累乘(1 - p)的结果求和就是空格子个数的期望
ans = sum(sum(row) for row in empty_prob)
print(f'{ans:.6f}')