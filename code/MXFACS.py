# let n = p1^a1 p2^a2 ... pk^ak
# n has (a1+1)*(a2+1)*...*(ak+1) divisors
# k = pi for some pi => we can factorize n and try all factors!!

max_sq = 40000
primes = []
is_composite = [False for i in range(max_sq)]
is_composite[0] = True
is_composite[1] = True
for i in range(2, max_sq):
    if not is_composite[i]:
        primes.append(i) #we list all primes <= max sqrt(n) for the factorization step
        for j in range(2, max_sq):
            if j*i >= max_sq:
                break
            is_composite[j*i] = True

t = int(input())

while t > 0:
    n = int(input()) 
    
    pi = []
    ai = []
    
    for p in primes:
        if p*p > n: #remaining factor of n must be a prime
            break
        
        cur_ai = 0
        while n%p == 0:
            n = n//p
            cur_ai+=1
            
        if cur_ai>0:
            pi.append(p)
            ai.append(cur_ai)
    if n>1:
        pi.append(n)
        ai.append(1)
        
    divisors_n = 1
    for a in ai:
        divisors_n *= (a+1)
    
    best_so_far = -1
    k = n
    
    for i in range(len(pi)):
        #what if k = pi[i] ?
        val = (divisors_n//(ai[i]+1))*ai[i]
        if val > best_so_far:
            k = pi[i]
            best_so_far = val
        
    print(k)
    t-= 1
