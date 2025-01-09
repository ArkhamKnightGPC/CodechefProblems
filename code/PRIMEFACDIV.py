t = int(input())

def gcd(x, y):
    return x if y == 0 else gcd(y, x%y)

for _ in range(t):
    inp = [int(x) for x in input().split()]
    A, B = inp[0], inp[1]

    g = gcd(A, B)
    while g > 1:
        B = B//g
        g = gcd(A, B)

    # if all prime factors of B are also in A
    # => if we keep dividing by gcd we reach B = 1
    print("YES" if B == 1 else "NO")
