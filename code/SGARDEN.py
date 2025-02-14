MOD = int(10**9 + 7)

maxn = int(10**5 + 4)
primes = []
find_prime_idx = [-1]*maxn

def sieve():
    is_composite = [False]*maxn
    for i in range(2, maxn):
        if not is_composite[i]:
            find_prime_idx[i] = len(primes) #we will need to access this index later...
            primes.append(i)
            j = 2*i
            while j < maxn:
                is_composite[j] = True
                j += i

def fastxp(a, b):
    if b == 0:
        return 1
    if b%2 == 1:
        return (a*fastxp(a, b-1))%MOD
    aux = fastxp(a, b//2)
    return (aux*aux)%MOD

sieve() #find all primes we may need to use in factorization
t = int(input())

for _ in range(t):

    prime_exponent_lcm = [0]*len(primes)

    n = int(input())
    A = [int(x)-1 for x in input().split()]

    cycle_lengths = [] # we will find length of all cycles in the permutation in O(n)
    mrk = [False]*n
    for i in range(n):
        if not mrk[i]:
            mrk[i] = True
            lgt = 1
            cur = A[i]
            while cur != i: #we tag positions until we close the cycle
                mrk[cur] = True
                lgt += 1
                cur = A[cur]
            cycle_lengths.append(lgt)

    ans = 1
    for lgt in cycle_lengths: # and find least common multiple of all cycle lengths
        # to do this we need factorization of lgt
        i = 0
        while primes[i]*primes[i] <= lgt:
            factor = 0
            while lgt%primes[i] == 0:
                lgt = lgt//primes[i]
                factor += 1
            prime_exponent_lcm[i] = max(prime_exponent_lcm[i], factor)
            i += 1
        lgt_idx = find_prime_idx[lgt]
        if lgt_idx != -1: #now factor remaining is prime
            prime_exponent_lcm[lgt_idx] = max(prime_exponent_lcm[lgt_idx], 1)

    ans = 1
    for i in range(len(primes)):
        ans = (ans*fastxp(primes[i], prime_exponent_lcm[i]))%MOD
    print(ans)