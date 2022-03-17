# import libraries
import sys,keyword
# displaying the python version used
print('Python Version: ',sys.version)
# displaying the python IDLE location
print('Python Interpreter Location:',sys.executable)
# displaying the module path
for dir in sys.path:
    print(dir)
# displaying the python keywords
for word in keyword.kwlist:
    print(word)
# displaying the knight from 0-4
print('Here are 5 Knights')
for i in range(5):
    print('Knight ('+str(i)+')')
# declaring variable gauss = 0
gauss = 0
# displaying the sum of numbers from 0 to 100
for num in range(101):
    # adding the values
    gauss = gauss + num
# displaying the values with 3 steps
# which prints the values 0,3,6,9
for i in range(0,10,3):
    print(i)
    
# displaying the sum of natural from 1 to 100
s = 0
for i in range(1,101):
    s = s + i
# displaying the result
print('The sum is',s)
# initalizing the variales with values
W,X,Y,Z = 10,15,20,25
# displaying the result
print(W,X,Y,Z)
# displaying the values by seperating with ,
print(W,X,Y,Z,sep=",")
# displaying the values by seperating with space( )
print(W,X,Y,Z,sep=" ")
# displaying the values by seperating with @
print(W,X,Y,Z,sep='@')
# declaring a list named phrase
phrase = ['We','are','great','coders','of','Python 3']
for i in range(len(phrase)):
    #displaying the elements of list with index values
    # Note: Here a[] is not defined, it should be phrase[i]
    print(i,a[i])
    