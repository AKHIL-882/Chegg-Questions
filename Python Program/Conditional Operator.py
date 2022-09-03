# getting user inputs
num_users = int(input())
update_direction = int(input())
# condition using conditional operators
num_users = num_users + 1 if update_direction == 3 else num_users - 1
# displaying the result
print('New value is:', num_users)