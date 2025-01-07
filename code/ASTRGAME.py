def mex(x):
    for i in range(0, s_sz*s_sz):
        if not(i in x):
            return i

def grundy_number(l, r):
    if l > r:
        return 0 #BASE CASE
    if dp[l][r] != -1:
        return dp[l][r] #MEMOIZATION
    aux = set()
    for lp in range(l, r+1):
        for rp in range(lp, r+1):
            if is_legal_substr[lp][rp]: #removing substr is a legal move!!
                aux.add(grundy_number(l, lp-1)^grundy_number(rp+1, r)) #DP RECURRENCE
    dp[l][r] = mex(aux)
    return dp[l][r]

t = int(input())

for _ in range(t):
    s = input()
    s_sz = len(s)

    n = int(input())

    dp = [[-1 for j in range(s_sz)] for i in range(s_sz)]
    is_legal_substr = [[False for j in range(s_sz)] for i in range(s_sz)]

    legal_substrings = set()
    for __ in range(n):
        dict_str = input()
        legal_substrings.add(dict_str)

    for l in range(s_sz):
        substr = ""
        for r in range(l, s_sz):
            substr += s[r]
            if substr in legal_substrings: #we precompute which substrings are legal to optimize dp transition!!
                is_legal_substr[l][r] = True

    # The game is an impartial game defined by string interval s(l..r)
    # => we can use Sprague-Grundy Theorem to determine the winner
    # we use dynamic programming to compute grundy numbers
    # BASE CASE: grundy number of empty interval is 0
    # RECURRENCE: dp[i][j] = MAX(dp[i, i'-1] XOR dp[j'+1, j]) where s(i'..j') is in legal_substrings
    # COMPLEXITY: O(N^2) states, O(N^2 + MEX) transition => O(N^4) solution (ok!!)
    ans = grundy_number(0, s_sz-1)

    print("Teddy" if ans > 0 else "Tracy")
    