# getting the input from the user
userMarks = int(input("Plesae Enter the Student's Grade: "))
# checking the marks entered by the student is under the 
# given range or not
if(userMarks<0 or userMarks>100):
    print("Incorrect entry")
else:
    # condition for grade A
    if(userMarks>=90 and userMarks<=100):
        print("Student's letter grade A")
    # condition for grade B
    if(userMarks>=78 and userMarks<=89):
        print("Student's letter grade B")
    # condition for grade C
    if(userMarks>=63 and userMarks<=77):
        print("Student's letter grade C")
    # condition for grade D
    if(userMarks>=51 and userMarks<=62):
        print("Student's letter grade D")
    # condition for grade F
    if(userMarks>=0 and userMarks<=50):
        print("Student's letter grade F")
    