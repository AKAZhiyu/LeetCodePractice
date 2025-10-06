n, total_weight = map(int, input().split())

weights, values = [], []

for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [[0] * (total_weight + 1) for _ in range(n)]

for i in range(weights[0], total_weight + 1):
    dp[0][i] = dp[0][i - weights[0]] + values[0]

for i in range(1, n):
    for j in range(total_weight + 1):
        if j < weights[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i][j - weights[i]] + values[i], dp[i - 1][j])

print(dp[-1][-1])





