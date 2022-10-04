# defining the function
def costElectricity(w,h,p):
    # calculating and returing the result
    return (w*h)/(1000*p)
    
    
# getting input from user
wattage = float(input())
hours = float(input())
costPerKilowatt = float(input())
# function calling and displaying the result
print(round(costElectricity(wattage,hours,costPerKilowatt),2))