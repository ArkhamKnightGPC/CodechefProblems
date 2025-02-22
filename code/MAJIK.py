tc = int(input())

for _ in range(tc):
    n = int(input())

    inp = input().split()
    p,q = int(inp[0]), int(inp[1])

    A = [int(x) for x in input().split()]
    A.sort()
    ans = A[n-1] - A[0]

    #two pointers, greedy solution: at each step pick element with maximal absolute value to increase answer
    l, r = 1, n-2
    ops = 0
    while (ops < p+q and l <= r):
        ops += 1
        if abs(A[l]) > abs(A[r]):
            ans += abs(A[l])
            l += 1
        else:
            ans += abs(A[r])
            r -= 1
    
    print(ans)
