import sys

INT_MAX = sys.maxsize 

#INPUT: n, graph G represented as weighted adjacency matirx W
#OUTPUT: shortest path matrix and predecessor node matrix

def FloydWarshall(n, W):
    currShortest = [row[:] for row in W]
    prevShortest = [row[:] for row in W]
    pred = [[None if W[i][j] == INT_MAX or i == j else i for j in range(n)] for i in range(n)]

    for x in range(n):
        for u in range(n):
            for v in range(n):
                if prevShortest[u][x] == INT_MAX or prevShortest[x][v] == INT_MAX:
                    currShortest[u][v] = prevShortest[u][v]
                elif prevShortest[u][v] <= prevShortest[u][x] + prevShortest[x][v]:
                    currShortest[u][v] = prevShortest[u][v]
                else:
                    currShortest[u][v] = prevShortest[u][x] + prevShortest[x][v]
                    pred[u][v] = pred[x][v]

        prevShortest = [row[:] for row in currShortest]

    return currShortest, pred

def main():
    # G: V={0,1,2,3} E={(0,1,3), (0,2,8), (1,3,1), (2,1,4), (3,0,2), (3,2,-5)}  <-(u, v, weight) 
    W = [[0, 3, 8, INT_MAX], 
         [INT_MAX, 0, INT_MAX, 1], 
         [INT_MAX, 4, 0, INT_MAX], 
         [2, INT_MAX, -5, 0]]
    
    shortest, pred = FloydWarshall(4, W)

    print("Shortest path matrix: ")
    for row in shortest:
        print(row)

    print("\nPredecessor matrix: ")
    for row in pred:
        print(row)

if __name__ == "__main__":
    main()