def partitionHoare(arr, p, q):
    pivot = arr[(p+q)//2]
    i=p-1
    j=q+1
    while(True):
        while(True):
            i+=1
            if arr[i] >= pivot:
                break
        while(True):
            j-=1
            if arr[j] <= pivot:
                break
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quickSort(arr, p, q):
    if p < q:
        idx = partitionHoare(arr, p, q)
        quickSort(arr, p, idx)
        quickSort(arr, idx+1, q)

def main():
    arr = [5,2,3,8,7,1,9,0,4,6]
    quickSort(arr, 0, len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()