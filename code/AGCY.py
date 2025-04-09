MAXN = 100003
x = [0]*MAXN #number of queries covering index i
sl = [0]*MAXN #sum of l for queries covering index i
#final value of a[i] = x[i]*(i+1) - sl[i]

help_x = [0]*MAXN #x = prefix sum of help_x
help_sl = [0]*MAXN #same idea!

def twoIntInput():
    inp = input().split()
    n1, n2 = int(inp[0]), int(inp[1])
    return n1, n2

t = int(input())

for _ in range(t):
    n,q = twoIntInput()

    for __ in range(q):
        l,r = twoIntInput()
        help_x[l] += 1
        help_x[r + 1] -= 1
        help_sl[l] += l
        help_sl[r + 1] -= l

    res = []
    for i in range(1, n+1):
        x[i] = x[i-1] + help_x[i]
        sl[i] = sl[i-1] + help_sl[i]
        res.append(str(x[i]*(i+1) - sl[i]))
    print(" ".join(res))

    for i in range(0, n+2):#RESET!!
        x[i], help_x[i], sl[i], help_sl[i] = 0, 0, 0, 0
    