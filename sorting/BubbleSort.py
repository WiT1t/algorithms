
def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    arr = [5,2,3,8,7,1,9,0,4,6]
    print(bubbleSort(arr))

if __name__ =="__main__":
    main()
            