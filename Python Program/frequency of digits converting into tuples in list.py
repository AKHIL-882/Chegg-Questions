# importing the libaries
from collections import Counter
# function delcaration
def get_duplicates_count(numbers_list):
    # count the values
    counts = dict(Counter(numbers))
    # counting the frequencies of values
    duplicates = [(key,value) for key, value in counts.items() if value > 1]
    # sorting the list
    duplicates.sort()
    # displaying the list
    return duplicates
    
#numbers = [9,5,1,4,5,1,7,7,3,2,8,1,9,4,1,2,3,9,7,6]
#numbers = [9,5,1,4,5,1,7,7]
# numbers = [1,2,3]

# use the below command to get values from user
numbers = [int(i) for i in input().split()]
# function calling and displaying the result
print(get_duplicates_count(numbers))
