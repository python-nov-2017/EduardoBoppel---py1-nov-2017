
for number in range(100, 100000):
       
    string = "Foo"
    
    #check for prime
    for i in range(2, number):
        if number % i == 0:
            string = "FooBar"
            break

    #check for perfect square
    for i in range(2, number):
        if float(number) / float(i) == i:
            string = "Bar"
            break

    
    print number, string
    
    
    
    