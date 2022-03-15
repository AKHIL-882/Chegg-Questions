playerDictionary={}
# addding user
for i in range(1,6):
    print("Enter player "+str(i)+"'s jersey number:")
    key=int(input())
    print("Enter player "+str(i)+"'s rating:")
    value=int(input())
    playerDictionary[key]=value
print("ROSTER")
for i in sorted(playerDictionary):
    print("Jersey number: "+str(i)+", Rating: "+str(playerDictionary[i]))
# menu 
while(1):
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("\nChoose an option:")
    n=input()
    if(n=="o"):
        print("ROSTER")
        for i in sorted(playerDictionary):
            print("Jersey number: "+str(i)+", Rating: "+str(playerDictionary[i]))
    elif(n=="a"):
        print("Enter a new player's jersey number:")
        key=int(input())
        print("Enter the player's rating:")
        value=int(input())
        playerDictionary[key]=value
    elif(n=="d"):
        print("Enter a jersey number:")
        key=int(input())
        playerDictionary.pop(key)
    elif(n=="u"):
        print("Enter a jersey number:")
        key=int(input())
        print("Enter a new rating for player:")
        value=int(input())
        playerDictionary[key]=value
    elif(n=="r"):
        print("Enter a rating:")
        rating=int(input())
        print("ABOVE "+str(rating))
        for i in sorted(playerDictionary):
            if(playerDictionary[i]>rating):
                print("Jersey number: "+str(i)+", Rating: "+str(playerDictionary[i]))
    else:
        exit(0)
    
    
    
    