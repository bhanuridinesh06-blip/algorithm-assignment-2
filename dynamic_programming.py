# Task 4: Dynamic Programming - 0/1 Knapsack
def knapsack_01(W, wt, val, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][W]

# Test
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(f"0/1 Knapsack Optimal Value: {knapsack_01(W, wt, val, n)}")
