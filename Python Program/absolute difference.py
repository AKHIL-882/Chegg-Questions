# function declartion
def max_array_diff(arr, n):
    # minimum element
    minElement = min(arr)
    # maximum element
    maxElement = max(arr)
    # returing the value
    return abs(minElement) + abs(maxElement)
# getting input value from user
arr = [int(i) for i in input().split()]
# function calling and displaying the result`
print(max_array_diff(arr, len(arr)))