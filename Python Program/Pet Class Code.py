# declaring the petClassClass
class petClass:
    # initializing
    def __init__(self):
        # declaring the arrays
        self.name = []
        self.type = []
        self.age = []
    # function to append to the arrays
    def add(self,name,typ,age):
        self.name.append(name)
        self.type.append(typ)
        self.age.append(age)

# main 
if __name__ == '__main__':
    # object creation
    petClass = petClass()
    # getting inputs from the user
    print("Enter name, type and age of your petClass:")
    nameOfPet = input("Name: ")
    typeOfPet = input("Type: ")
    ageOfPet = input("Age: ")
    # adding the values to the arrays
    petClass.add(nameOfPet,typeOfPet,ageOfPet)
    # iterate until user enters quit
    while(1):
        print('Enter "quit" to stop entering. Anything else to continue.')
        # getting user input text
        userText = input()
        if userText == "quit":
            break
        print("Enter name, type and age of your petClass:")
        # getting inputs from the user
        nameOfPet = input("Name: ")
        typeOfPet = input("Type: ")
        ageOfPet = input("Age: ")
        # adding the values to the arrays
        petClass.add(nameOfPet,typeOfPet,ageOfPet)
    # displaying the summary of the information provided
    print("\n\nSUMMARY:")
    print("--------")
    # displaying data
    for name,typ,age in zip(petClass.name,petClass.type,petClass.age):
        print("Name: {}, Type: {}, Age: {}.".format(name,typ,age))
        
        
        
        
        