# reading the file
fileRead=open("data.txt","r")
# declaring the list of weights and heights
weights = []
heights = []
# iterating over the file data
for line in fileRead:
    # spliting the data 
    weightsData,heightsData = line.split(",")
    # appending weight into weights list
    weights.append(int(weightsData.strip()))
    # appending height into heights list
    heights.append(int(heightsData.strip()))
# displaying the Average    
print("Average weight: ",sum(weights)/len(weights))
print("Average height: ",sum(heights)/len(weights))