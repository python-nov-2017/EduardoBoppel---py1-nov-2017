list1 = [2,3,1,7,4,12]
list2 = ['magical','unicorns']
list3 = ['magical unicorns',19,'hello',98.98,'world']

input = list3


total = 0
string = ""

for element in input:
    if isinstance(element, (int, long, float)):
        total += element

    elif isinstance(element, (str)):
        string += element
            
        
if total != 0 and len(string) > 0:
    print "The list you entered is of the MIXED type"
    print "Total:", total
    print "New String:", string
    
elif total > 0:
    print "The list you entered is of the INTEGER type"
    print "Total:", total

else:
    print "The list you entered is of the STRING type"
    print "New String:", string
