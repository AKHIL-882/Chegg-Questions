# function declaration
def minDiff(arr):
    n = len(arr)
    # sorting the values
    arr.sort()
    sum = 0
    # getting the differences
    sum += abs(arr[0] - arr[1]);
    sum += abs(arr[n - 1] - arr[n - 2]);
    for i in range(1, n - 1):
        sum += min(abs(arr[i] - arr[i - 1]),
                  abs(arr[i] - arr[i + 1]))
    # returning the result
    return sum;
# main function
if __name__ == '__main__':
    # getting the size form the user
    n = int(input())
    # getting the values
    arr = [int(n) for n in input().split()]
    # displaying the result
    print(minDiff(arr))