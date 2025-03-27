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
        Q = insert(Q, v)
    while len(Q) > 0:
        u = extract_min(Q, shortest)
        for [v,w] in G[u]:
            shortest, pred = relax(G, shortest, pred, u, v)
    
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

def insert(Q, v):
    Q.append(v)
    return Q

def extract_min(Q, shortest):
    min = INT_MAX
    min_node = 0
    for v in Q:
        if min > shortest[v]:
            min = shortest[v]
            min_node = v
    Q.remove(min_node)
    return min_node

def main():
    G = {0: [(1,3), (2,8)],
         1: [(3, 1)],
         2: [(1,4)],
         3: [(0,2), (2, -5)]}
    
    shortest, pred = Dijkstra(G, 1)
    print("Shortest paths:")
    print(shortest)
    print("\nPredecessors: ")
    print(pred)

if __name__ == "__main__":
    main()