#MULTIPLES

#PART 1 - print all odd numbers from 1 to 1000
for count in range(1, 1000):
    if count % 2 == 1:
        print count

#PART 2
for count in range (5, 1000001, 5):
    print count


#SUM LIST
a = [1, 2, 5, 10, 255, 3]

# using sum() function
print sum(a)  

#using a loop 
total = 0  
for element in a:
    total += element
print total



#AVERAGE LIST
a = [1, 2, 5, 10, 255, 3]
total = sum(a)
avg = total / len(a)
print avg