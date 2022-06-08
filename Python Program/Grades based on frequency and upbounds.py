# assing the number of subjects
n = 5
userMarks = []
# function to check whether the marks are not in 
# the given range
def userMarksCheck(mark):
    print("Enter the marks again: ")
    mark = int(input())
    if(mark<0 or mark>100):
        userMarksCheck(mark)
    else:
        userMarks.append(mark)
# getting the marks from the user
for i in range(n):
    marksStudent = int(input("Enter the subject marks:" ))
    if(marksStudent<0 or marksStudent>100):
        userMarksCheck(marksStudent)
    else:
        userMarks.append(marksStudent)
subjectList = []
count=0
#print(userMarks)
# appending and assigning the subject 
# based on marks
d = []
counta,countb,countc,countd=0,0,0,0
for i in userMarks:
    if(i>=85 and i<=100):
       d.append("A")
    elif(i>=75 and i<=84):
        d.append("B")
    elif(i>=50 and i<=74):
        d.append("C")
    else:
        d.append("D")
#print(d)
# finding the frequency of each grade
def CountFrequency(d):
	freq = {}
	for items in d:
		freq[items] = d.count(items)
	for key, value in freq.items():
		print ("Number of % s Subjects: % s"%(key, value))
CountFrequency(d)
# displaying the subject if not found
u = ["A","B","C","D"]
for i in u:
    if(i not in d):
        print("Number of",i,"Subjects:",0)
        
        