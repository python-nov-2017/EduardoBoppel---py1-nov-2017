sI = 45
mI = 100
bI = 455
eI = 0
spI = -230
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


value = spL
print value


#INTEGER - if integer is greater than 100, print "big number", else print "small number"
if isinstance(value, (int, long, float)):
    if value >= 100 or value <= -100:
        print "Thats a big number"
    else:
        print "Thats a small number"

#STRING - If string is greater than 50 characters, print "long sentence", else print "short sentence"    
if isinstance(value, str):
    if len(value) >= 50:
        print "Thats a long sentence"
    else:
        print "Thats a short sentence"
    
    
#LIST - if list length is greater than 10, print "big list", else "short list"
if isinstance(value, list):
    if len(value) >= 10:
        print "That's a long list"
    else:
        print "That's a short list"