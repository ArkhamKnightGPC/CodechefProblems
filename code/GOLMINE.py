eps = 10**(-9)

t = int(input())
M = []

class mine:
    def __init__(self, gi, ai, bi):
        self.gold = gi
        self.speedA = gi/ai
        self.speedB = gi/bi

def get_orderA():
    global M
    #return list of indexes in M with speedA in decreasing order
    orderA = sorted(range(len(M)), key = lambda i: M[i].speedA, reverse=True)
    return orderA

def get_orderB():
    global M
    #return list of indexes in M with speedB in decreasing order
    orderB = sorted(range(len(M)), key = lambda i: M[i].speedB, reverse=True)
    return orderB

for _ in range(t):
    n = int(input())
    M = [] #reset M at the start of each test case
    for i in range(n):
        gi, ai, bi = input().split()
        M.append(mine(float(gi), float(ai), float(bi)))

    orderA = get_orderA() #each miner will greedily prefer mines with max speed
    orderB = get_orderB()
    mines_left = n

    idxA, ansA = 0, 0
    idxB, ansB = 0, 0
    while True:

        while M[idxA].gold <= eps:
            idxA += 1
            if idxA == len(M):
                break

        while M[idxB].gold <= eps:
            idxB += 1
            if idxB == len(M):
                break

        if idxA == len(M) or idxB == len(M):
            break

        gainA, gainB = 0, 0
        if idxA == idxB: #they are both on the same mine!
            timeAB = M[idxA].gold/(M[idxA].speedA + M[idxB].speedB)
            gainA = timeAB * M[idxA].speedA
            gainB = timeAB * M[idxB].speedB
        else:
            timeA = M[idxA].gold/M[idxA]
            timeB = M[idxB].gold/M[idxB]
            if timeA < timeB: # A will finish before B
                gainA = timeA * M[idxA].speedA
                gainB = timeA * M[idxB].speedB
            else:
                gainA = timeB * M[idxA].speedA
                gainB = timeB * M[idxB].speedB
            
        ansA += gainA
        ansB += gainB
        M[idxA].gold -= gainA
        M[idxB].gold -= gainB
    
    print(f"{ansA} {ansB}")
    