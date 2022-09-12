# user list
l = []
while(1):
  print('***************')
  # getting the user input
  another = int(input())
  l.append(another)
  # slicing the list
  res1 = l[-3:]
  if(sum(res1)==10):
      print("\n Last Sum is equal to 10 \n Removing the last 2 numbers")
      l = l[:-2]
  # slicing the list
  res2 = l[-4:]
  if(sum(res2)==20):
      print("\n Last Sum is equal to 20 \n Removing the last 4 numbers")
      l = l[:-len(l)]
  print("List elements ",l)
  # win condition
  if(sum(l)==44):
    print('You Won !!!')
    break
  else:
      continue
  
  