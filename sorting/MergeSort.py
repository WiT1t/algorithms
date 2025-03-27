def merge(A, i, B, j):
    if len(A) - i == 0: return [B[x] for x in range(j, len(B))]
    if len(B) - j == 0: return [A[x] for x in range(i, len(A))]
    if(A[i] < B[j]):
        return [A[i]] + merge(A, i+1, B, j)
    return [B[j]] + merge(A, i, B, j+1)

def mergeSort(arr):
    if len(arr) == 1: return arr

    A = [arr[i] for i in range(len(arr)//2)]
    B = [arr[i] for i in range(len(arr)//2, len(arr))]
    A = mergeSort(A)
    B = mergeSort(B)
    return merge(A, 0, B, 0)

def main():
    arr = [5,2,3,8,7,1,9,0,4,6]
    print(mergeSort(arr))

if __name__ =="__main__":
    main()