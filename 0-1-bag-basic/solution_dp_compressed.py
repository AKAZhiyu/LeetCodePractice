n, bagweight = map(int, input().split())

weight = list(map(int, input().split()))
value = list(map(int, input().split()))

# the maximum value from 0 - i when have the capacity j
dp = [0] * (bagweight + 1)

for i in range(0, n):
    for j in range(bagweight, weight[i] - 1, -1):
            dp[j] = max(dp[j], value[i] + dp[j - weight[i]])

print(dp[bagweight])

