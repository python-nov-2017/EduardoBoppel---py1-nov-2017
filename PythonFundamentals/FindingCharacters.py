# input
word_list = ['hello','world', 'my','name','is','Anna']
char = 'o'

# output
new_list = []


for word in word_list:
    if word.find(char) >= 0:
        new_list.append(word)

print new_list
