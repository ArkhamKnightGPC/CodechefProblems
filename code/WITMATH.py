import random

def fastxp(base, expo, modn):
    result = 1
    while expo > 0: 
        if expo % 2 == 1: 
            result = (result * base) % modn
            expo -= 1
        else:
            result = (result * result) % modn 
            expo = expo//2
    return result
    
def miller_rabin(n):
    s = 0
    d = n-1
    #we factorize n-1 = d * 2^s with n,d odd
    while d%2 == 0:
        d = d//2
        s += 1
        
    for i in range(3): # we try 3 random bases
        base = random.randrange(2, n)
        aux = fastxp(base, d, n)
        flag = True if ((aux-1)%n == 0 or (aux+1)%n == 0)else False
        for expo in range(2, s+1):
            aux = (aux*aux)%n # we reuse previous result instead of calling fastxp
            flag = True if (aux+1)%n == 0 else flag
            if flag:
                break
        if not flag:
            return False #failure => n is not prime
    return True #no failure => n is very likely prime
    
t = int(input())
for _ in range(t):
    
    n = int(input())
    
    # we want largest prime <= n where 2 <= n <= 10^18
    # for this prime p, we have phi(p)/p = (p-1)/p
    # we use O(lg n) Miller-Rabin probabilistic primality test
    if n == 2:
        print(2) #n=2 is a special case
    else:    
        if n%2 == 0:
            n -= 1
        while not miller_rabin(n) and n > 2: #this loop will run ~O(lg n) times => O(lg^2 n) solution
            n -= 2
        print(n)
