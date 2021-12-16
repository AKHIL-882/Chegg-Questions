# Mistake:1 File opening function have to be used
fhand =open("testing.txt")
count = 0
for line in fhand:
    # Mistake:2 split fuction have parentesis not square brakets
    words = line.split()
    if len(words)==0 and words[0]!='Paragraph':
        continue
    # Mistake:3 Condition to count the lines
    if words[0]=='Paragraph':
        count = count+1
# Mistake:4 Displaying the count
print("There were",count)