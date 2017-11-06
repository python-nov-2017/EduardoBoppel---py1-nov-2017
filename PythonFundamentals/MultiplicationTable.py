row = ["x", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


string = ""

for index in row:
    string += str(index) + "  "
print string


for index in row[1:]:

    string = str(index)+ "  "
    
    for num in row[1:]:
        value = num * (index)
        string += str(value) + "  "
    
    print string

 



