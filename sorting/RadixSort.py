def countingSort(arr, exp):
    count = [0] * 10
    output = [0] * len(arr)

    for i in arr:
        index = (i // exp)%10
        count[index]+=1
    for i in range(1,10):
        count[i] += count[i-1]
    for i in reversed(arr):
        index = (i // exp)%10
        output[count[index]-1] = i
        count[index]-=1
    return output

def radixSort(arr):
    maxVal = max(arr)
    exp = 1
    while maxVal // exp > 0:
        arr = countingSort(arr, exp)
        exp*=10
    return arr


def main():
    arr = [123, 871, 239, 2320, 11, 234, 678, 1002]
    print(radixSort(arr))

if __name__ == "__main__":
    main()