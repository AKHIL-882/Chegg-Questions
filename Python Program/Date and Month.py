# getting month and date from the user
month =  input ("Enter the name of the  month:")
day   =  int (input ("Enter the day number:"))

# condition to check the seasons
if  month == "January" or month == "February":
   season   =  "Summer"
elif   month == "March":
   if  day  <  20:
     season = "Summer"
   else :
     season = "Autumn"
elif   month == "April" or month == "May":
   season   =  "Autumn"
elif   month == "June":
   if  day  <  21:
     season = "Autumn"
   else :
     season = "Winter"
elif   month == "July" or month == "August":
   season   =  "Winter"
elif   month == "September":
   if  day  <  22:
     season = "Winter"
   else :
     season = "Spring"
elif   month == "October"  or month == "November":
   season   =  "Spring"
elif   month == "December":
   if  day  <  21:
     season = "Spring"
   else :
     season = "Summer"

# displaying the result
print (month,day,"is a",season)


