import sys

INT_MAX = sys.maxsize

#INPUT: List of vertices V, List of Edges with weights [u,v,wiegth] E, source vertex s (V[s])
#OUTPUT: array shortest where shortest[i] is the length of the shortest path from V[s] to V[i],
#        array pred where pred[i] is the predecessor of V[i] on the shortest path from V[s] to V[i]

def Dijkstra(G, s):
    shortest = [INT_MAX] * len(G)
    shortest[s] = 0
    pred = [None] * len(G)
    Q = []
    for v in range(len(G)):
        Q = insert(Q, shortest, v)
    while len(Q) > 0:
        u, Q = extract_min(Q, shortest)
        for [v,w] in G[u]:
            shortest, pred = relax(G, shortest, pred, u, v)
            Q = decrease_weight(Q, shortest, v)
    
    return shortest, pred


def relax(G, shortest, pred, u, v):
    w = find_weight(G, u, v)
    if w == None: return shortest, pred
    if shortest[u] != INT_MAX:
        if shortest[v] > shortest[u] + w:
            shortest[v] = shortest[u] + w
            pred[v] = u
    return shortest, pred

def find_weight(G, u, v):
    for (a,b) in G[u]:
        if a == v:
            return b
    return None

def insert(Q, shortest, v):
    Q.append(v)
    idx = len(Q) -1
    while(shortest[Q[idx]] < shortest[Q[idx//2]]):
        Q[idx], Q[idx//2] = Q[idx//2], Q[idx]
        idx = idx//2

    return Q

def decrease_weight(Q, shortest, v):
    idx=0
    if len(Q) == 0: return Q
    while Q[idx] != v:
        idx+=1
        if idx == len(Q): return Q
    
    while(shortest[Q[idx]] < shortest[Q[idx//2]]):
        Q[idx], Q[idx//2] = Q[idx//2], Q[idx]
        idx = idx//2

    return Q

def extract_min(Q, shortest):
    u = Q[0]
    Q[0] = Q[len(Q)-1]
    Q.pop()
    idx = 1
    while 2*idx -1 < len(Q):
        if 2*idx < len(Q):
            if shortest[2*idx-1] > shortest[2*idx]:
                Q[idx - 1], Q[2*idx] = Q[2*idx], Q[idx - 1]
                idx  = 2*idx + 1
            else:
                Q[idx - 1], Q[2*idx - 1] = Q[2*idx - 1], Q[idx - 1]
                idx  = 2*idx
        else:
                Q[idx - 1], Q[2*idx - 1] = Q[2*idx - 1], Q[idx - 1]
                idx  = 2*idx
    return u, Q
            

def main():
    G = {0: [(1,3), (2,8)],
         1: [(3, 1)],
         2: [(1,4)],
         3: [(0,2), (2, -5)]}
    
    shortest, pred = Dijkstra(G, 2)
    print("Shortest paths:")
    print(shortest)
    print("\nPredecessors: ")
    print(pred)

if __name__ == "__main__":
    main()