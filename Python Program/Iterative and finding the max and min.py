# defining the function
def integer_list_input():
    # getting the number of values from user
    testCases = int(input('Enter number of test score you want to enter: '))
    scores=[]
    i=0
    # iterating over the given range 
    while(i<testCases):
         # getting the scores from the user
         score=input('Enter test scores: ')
         if score=='':
             break
         # if the score is grether than 100 or
         # less then 0 continue
         elif int(score)>100 or int(score)<0:
            print('Test scores must be positive ')
            continue
         # append the score to the list
         else :
            scores.append(int(score))
         i=i+1
    # displaying the result
    print('Minimum: ', min(scores))
    print('Maximum: ', max(scores))
integer_list_input()