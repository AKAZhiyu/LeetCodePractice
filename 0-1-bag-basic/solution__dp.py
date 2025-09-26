n, bagweight = map(int, input().split())

weight = list(map(int, input().split()))
value = list(map(int, input().split()))

# the maximum value from 0 - i when have the capacity j
dp = [[0] * (bagweight + 1) for _ in range(n)]

for i in range(bagweight + 1):
    if i < weight[0]:
        dp[0][i] = 0
    else:
        dp[0][i] = value[0]

for i in range(1, n):
    for j in range(bagweight + 1):
        if weight[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], value[i] + dp[i - 1][j - weight[i]])

print(dp[-1][-1])

