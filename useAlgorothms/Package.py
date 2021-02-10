# package problem


def dp_package(volume, size):
    weight = [1, 3, 4]
    value = [1500, 2000, 3000]
    dp = [[0 for i in range(volume + 1)] for k in range(size + 1)]
    print(dp)
    for i in range(1,size + 1):
        for j in range(1,volume + 1):
            if weight[i-1] <= j:
                dp[i][j] = max(value[i - 1] + dp[i - 1][j - weight[i - 1]], dp[i - 1][j]) 
                print(i,j,dp[i][j])
            else:
                dp[i][j] = dp[i - 1][j]
    for j in dp:
        print(j)
    return dp


if __name__ == '__main__':
    volume = 4
    n = 3
    dp = dp_package(volume, n)
