def partitionLomuto(arr, p, q):
    pivot = arr[q]
    s = p
    for i in range(p, q):
        if pivot > arr[i]:
            arr[i], arr[s] = arr[s], arr[i]
            s+=1
    arr[s], arr[q] = arr[q],arr[s]
    return s
    

def quickSort(arr, p, q):
    if p < q:
        idx = partitionLomuto(arr, p, q)
        quickSort(arr, p, idx-1)
        quickSort(arr, idx+1, q)

def main():
    arr = [5,2,3,8,7,1,9,0,4,6]
    quickSort(arr, 0, len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()