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

# longest common sequence

def dp_lcs(str1,str2):
    dp = [[0 for i in range(len(str2))] for k in range(len(str1))]
    lcs = ""
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i]==str2[j]:
                dp[i][j]=dp[i-1][j]+1
                # if str1[i] repeat
                if str1[i] in lcs:
                    continue
                else:
                    lcs+=str1[i]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    for j in dp:
        print(j)
    print(lcs)
    return dp



if __name__ == '__main__':
    volume = 4
    n = 3
    dp = dp_package(volume, n)
    dp2 = dp_lcs("bluess","cluess")