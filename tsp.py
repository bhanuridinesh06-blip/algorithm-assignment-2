# Task 5: Traveling Salesman Problem (Held-Karp)
def tsp(mask, pos, n, dist, memo):
    if mask == (1 << n) - 1:
        return dist[pos][0]
    if (mask, pos) in memo:
        return memo[(mask, pos)]
    ans = float('inf')
    for city in range(n):
        if (mask & (1 << city)) == 0:
            new_ans = dist[pos][city] + tsp(mask | (1 << city), city, n, dist, memo)
            ans = min(ans, new_ans)
    memo[(mask, pos)] = ans
    return ans

graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
print(f"TSP Minimum Cost: {tsp(1, 0, 4, graph, {})}")
