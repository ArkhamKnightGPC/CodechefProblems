inp = [int(x) for x in input().split()]
n,m,q = inp[0], inp[1], inp[2]

adj_list = [ [] for i in range(n+1)]
state = [0 for i in range(n+1)] # 0 = not frozen, 1 = frozen
for i in range(m):
    inp = [int(x) for x in input().split()]
    u,v = inp[0],inp[1]
    adj_list[u].append(v)
    adj_list[v].append(u)

nodes_to_freeze = [] # stack of nodes where we need to propagate FREEZE

for i in range(q):
    inp = [int(x) for x in input().split()]
    t,x = inp[0], inp[1]
    if t == 1: #FREEZE node x
        if state[x] == 0:
            state[x] = 1
            nodes_to_freeze.append(x)
    elif t == 2: #PASS x time
        while x > 0 and len(nodes_to_freeze)>0:
            #at each time, we need to process all nodes in nodes_to_freeze
            new_nodes_to_freeze = [] #we create a separate list for nodes that will change state
            for u in nodes_to_freeze:
                for v in adj_list[u]:
                    if state[v]:
                        pass
                    else: #lets freeze v
                        state[v] = 1
                        new_nodes_to_freeze.append(v)
            nodes_to_freeze = new_nodes_to_freeze
            x -= 1
            
    else: #QUERY node x state
        print("YES" if state[x] else "NO")
        
#Since each node freezes at most once => inserted and popped from nodes_to_freeze at most once
# => O(n+m) amortized
