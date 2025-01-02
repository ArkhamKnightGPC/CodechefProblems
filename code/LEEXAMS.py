t = int(input())

def count_bits(x):
    aux = 0
    while x>0:
        x -= (x&(-x))
        aux += 1
    return aux

for _ in range(t):
    n = int(input())
    A, B, P = [0]*(n+1), [0]*(n+1), [0]*(n+1)
    max_label = 0
    for i in range(1, n+1):
        inp = input().split()
        P[i], A[i], B[i] = int(inp[0])/100.0, int(inp[1])-1, int(inp[2])-1
        max_label = max(max_label, max(A[i], B[i])+1)
    if n > 16: #1<=A[i],B[i]<=16 => impossible to have n>16 unique labels
        print(0)
    else: #there is at most 2^n <= 7 10^4 possibilites
        num_cases = (1<<max_label)
        #dp[i][mask] = probability to obtain labels in mask with tickets 1,...,i
        dp = [[0 for ___ in range(num_cases)] for __ in range(n + 1)]
        dp[0][0] = 1 #BASE CASE: empty mask, no tickets
        for i in range(1, n+1):
            for j in range(0, num_cases):
                if dp[i - 1][j] > 0:
                    if (j & (1 << A[i])) == 0: #we can add ticket i with label A[i]
                        dp[i][j | (1 << A[i])] += dp[i - 1][j]*P[i]
                    if (j & (1 << B[i])) == 0: #we can add ticket i with label B[i]
                        dp[i][j | (1 << B[i])] += dp[i - 1][j]*(1 - P[i])
        # solution runs in O(n*2^n) time (ok!)
        ans = 0
        for j in range(1, num_cases):
            if count_bits(j)==n:
                ans += dp[n][j]
        print(ans)
