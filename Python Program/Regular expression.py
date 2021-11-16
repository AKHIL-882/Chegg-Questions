# importing the regular expression
import re
# getting the user input string
userText = input()
# declaring the patter to find 
pattern = "\s\d{3}\s{2}[a-z]{2}"
# mapping and checking the conditin
if(re.findall(pattern, userText)):
  # display if match
  print("Match")
else:
  # display if not match
  print("No match")