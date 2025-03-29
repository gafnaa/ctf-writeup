def min_path_sum(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]
    
    dp[0][0] = grid[0][0]
    
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[-1][-1]

# Input dari user
size = input().strip().split()
rows, cols = int(size[0]), int(size[1])
values = list(map(int, input().strip().split()))

grid = [values[i * cols:(i + 1) * cols] for i in range(rows)]

print(min_path_sum(grid))
