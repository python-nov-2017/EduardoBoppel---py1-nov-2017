#FIRST EXERCISE - FIND AND REPLACE
string = "It's thanksgiving day. It's my birthday,too!"
word = "day"

count = string.count(word)
print 'The word "day" appears {} times'.format(count)

firstPosition = string.find(word)
print 'Its first index is', firstPosition

newString = string.replace(word, "month")
print string
print newString


#SECOND EXERCISE - MIN AND MAX
x = [2, 54, -2, 7, 12, 98]
print "The minimum value is", min(x)
print "The maximum value is", max(x)



#THIRD EXERCISE - FIRST AND LAST
x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print x[0]
print x[len(x)-1]
newX = []
newX.append(x[0])
newX.append(x[len(x)-1])
print newX 


#FOURTH EXERCISE - NEW LIST
x = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
x.sort()
print x


length = len(x)/2
newX = []
newX.append(x[0:length])
newX.extend(x[length:])
print newX





