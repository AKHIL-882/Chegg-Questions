# main method 
def main():
    scores = input("Enter five test scores: ")
    # getting the scores from user
    return [int(num) for num in scores.split(" ")]

# function to determine grade 
def determineGrade(num):
    # assigining the grade based on score
    if 90 <= num <= 100:
        gradeChar = "A"
    elif 80 <= num <= 89:
        gradeChar = "B"
    elif 70 <= num <= 79:
        gradeChar = "C"
    elif 60 <= num <= 69:
        gradeChar = "D"
    else:
        gradeChar = "F"
    return gradeChar

# function to calculate average
def calcAverage(grades):
    # averaging
    average = sum(grades) / len(grades)
    grade = determineGrade(average)
    # final result
    print("The average is: {:.1f} and the grade is {}".format(average, grade))

# function to calculate score for each grade
def gradeForScore(num, gradeChar):
    print("{:.1f} is {}\n".format(num, gradeChar))

# lst as main
lst = main()
#determining the score
for n in lst:
    gradeForScore(n, determineGrade(n))
# function calling
calcAverage(lst)


