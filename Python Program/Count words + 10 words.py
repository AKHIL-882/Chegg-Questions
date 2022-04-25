# importing the libraries
from collections import Counter
# defining the function 
def countWords(userInput):
   word_count = 1
   # for loop to iterate over the string
   for i in range(len(userInput)):
      # removing the spaces, next line and tab space.
      if(userInput[i] == ' ' or userInput == '\n' or userInput == '\t'):
         # counting the words
         word_count += 1
    # returing the count
   return word_count
 
# getting the string from user
userInput = input("Enter the string: ")
# calling the function to find the words
total = countWords(userInput)
# display in the count of words
print("Total Number of Words in the string are: ", total)
# creating the list of words 
word_list = userInput.split()
# counting the words
word_count = Counter(word_list)
# displaying the 10 words
print(word_count.most_common(10))

