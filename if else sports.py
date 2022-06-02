# getting input from user
nGameCount = int(input())
# defining the conditions
if(nGameCount>=60):
    print('Supernatural')
elif(nGameCount>=45 and nGameCount<=59):
    print('Wizard')
elif(nGameCount>=30 and nGameCount<=44):
    print('Expert')
elif(nGameCount>=15 and nGameCount<=29):
    print('Novice')
else:
    print('Noob')