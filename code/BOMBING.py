inp = input().split()
n,m = int(inp[0]), int(inp[1])

# 1 <= n <= 10**9 is too much!! we must modify ranges and answer queries offline!!
queries = []
all_idx = []
sys_l = []
sys_r = []
for _ in range(m):
    inp = input().split()
    queries.append(inp)
    if inp[0]=="P":
        sys_l.append(int(inp[1]))
        sys_r.append(int(inp[2]))
        all_idx.append(sys_l[-1])
        #all_idx.append(sys_r[-1])
        all_idx.append(sys_r[-1]+1)
    elif inp[0]=="M":
        i,d = int(inp[1])-1, int(inp[2])
        sys_l[i] += d
        sys_r[i] += d
        all_idx.append(sys_l[i])
        all_idx.append(sys_r[i]+1)
    else:
        all_idx.append(int(inp[1]))
all_idx.sort()#now we replace indexes by index in all_idx to process queries!!
idx_dict = {}
for i in range(len(all_idx)):
    idx_dict[all_idx[i]] = i+1 #we add 1 to avoid the 0 index

n = len(all_idx)+1
fenwick = [0]*(n+4)
#consider A[i] = number of systems covering index i
#let B[i] = A[i]-A[i-1]
#we build fenwick tree over B
# 1) update [l,r] +1 => B[l]+=1 and B[r+1]-=1
# 2) update [l,r] -1 => B[l]-=1 and B[r+1]+=1
# 3) query x => B[1]+...+B[x]

def upt(idx, val):
    while idx <= n+2:
        fenwick[idx] += val
        idx += (idx&(-idx))

def query(idx):
    aux = 0
    while idx > 0:
        aux += fenwick[idx]
        idx -= (idx&(-idx))
    return aux

sys_l = [0]
sys_r = [0]
for i in range(m):
    inp = queries[i]
    if inp[0]=="P":
        u,v = int(inp[1]), int(inp[2])
        upt(idx_dict[u], 1)
        upt(idx_dict[v+1], -1)
        sys_l.append(u)
        sys_r.append(v)
    elif inp[0]=="M":
        i,d = int(inp[1]), int(inp[2])
        old_l = sys_l[i]
        old_r = sys_r[i]
        upt(idx_dict[old_l], -1)
        upt(idx_dict[old_r+1], +1)
        sys_l[i] = old_l+d
        sys_r[i] = old_r+d
        upt(idx_dict[sys_l[i]], +1)
        upt(idx_dict[sys_r[i]+1], -1)
    else:
        x = int(inp[1])
        print(query(idx_dict[x]))
    
