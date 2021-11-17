# defing the function
def smallestNumber(array, start, end):
    # conditions
    if (start > end):
        return end + 1
    if (start != array[start]):
        return start;
    mid = int((start + end) / 2)
    if (array[mid] == mid):
        return smallestNumber(array,mid+1, end)
    return smallestNumber(array,start, mid)
# taking input from user
arr = [int(n) for n in input().split()]
# finding the length
n = len(arr)
# displaying the result
print("The smallest missing element is ",smallestNumber(arr, 0, n-1))