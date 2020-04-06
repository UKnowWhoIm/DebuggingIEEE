from math import gcd

t=int(input())
for _ in range(t):
    # 'no' should be 'n'
    n=int(input())
    # 'ad' should be 'adj'
    adj=[list() for x in range(n)]
    for i in range(n-1):
        # Intendation fixed
        u,v=map(int,input().strip().split())
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    # str should be int
    v=list(map(int,input().strip().split()))
    # ')' is missing, str should be int
    m=list(map(int,input().strip().split()))
    factors=[0]*n
    leaves=[]
    # parent by default should be -1
    parent=[-1]*n
    queue=[0]
    for i in queue:
        children=set(adj[i])-set([parent[i]])
        if parent[i]==-1:
            # Indentation fixed
            factors[i]=v[i]
        else:
            # Indentation fixed, ']' is added after [parent[i]
            factors[i]=gcd(factors[parent[i]], v[i])
        if (len(children)<=0):
            # Indentation fixed, 'leavs' iscorrected to 'leaves'
            leaves.append(i)
        for q in children:
            # Indentation fixed
            parent[q]=i
            # Indentation fixed
            queue.append(q)
    # sorted returns a sorted arr without changing original arr
    leaves = sorted(leaves)
    re=[m[i]-gcd(m[i],factors[i]) for i in leaves]
    # To print space seperated values
    for x in re:
        print(x, end=' ')
