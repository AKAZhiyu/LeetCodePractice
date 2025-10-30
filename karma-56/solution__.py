c, n = input().split(" ")
c, n = int(c), int(n)

weights = [int(x) for x in input().split(" ")]
values = [int(x) for x in input().split(" ") if x]
nums = [int(x) for x in input().split(" ")]

dp = [0] * (c + 1)

for i in range(n):
    for j in range(c, weights[i] - 1, -1):
        for k in range(1, nums[i] + 1):
            if weights[i] * k > j:
                break
            dp[j] = max(dp[j], dp[j - weights[i] * k] + k * values[i])


print(dp[-1])
