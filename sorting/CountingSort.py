
#upperBoud: first integer greater than all the integers in arr
def countingSort(arr, upperBound):
    countArr = [0] * upperBound
    result= []

    for i in range(len(arr)):
        countArr[arr[i]]+=1
    for i in range(upperBound):
        while countArr[i] > 0:
            result.append(i)
            countArr[i]-=1
    return result

def main():
    arr = [5,2,3,8,7,1,9,0,4,6]
    print(countingSort(arr, 10))

if __name__ == "__main__":
    main()