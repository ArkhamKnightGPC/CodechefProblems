t = int(input())

#we start with a window of size 1 on element N
#at each step, we expand window to include N-1,N-2,...

while t>0:
    n = int(input())
    A = [int(x) for x in input().split()]
    
    left_of_N = [False for i in range(n+1)] #will tell us in which direct to extend window
    iN = 0
    for i in range(n):
        ai = A[i]
        if ai == n:
            iN = i 
            break
        else:
            left_of_N[ai] = True
    
    in_window = [False for i in range(n+1)]
    ans = 1 #max valid window size
    l, r = iN, iN #current window pointers
    min_in_window = n #smallest element in window, we use this check if window is valid
    for i in range(1, n-1):
        x = n - i #lets consider window with elements x,x+1,...,n (2<= x <n)
        if not in_window[x]: #we must expand window to include x
            if left_of_N[x]:
                while A[l] != x:
                    l -= 1
                    in_window[A[l]] = True
                    min_in_window = min(min_in_window, A[l])
            else: #must be to the right
                while A[r] != x:
                    r += 1
                    in_window[A[r]] = True
                    min_in_window = min(min_in_window, A[r])
        if min_in_window == x:
            ans = r-l+1
    print(ans)
    t -= 1
