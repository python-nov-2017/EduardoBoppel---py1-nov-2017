def odd_even():
    for number in range(1, 2000):
        string = "Number is {}. ".format(number)
        if number%2 != 0:
            string += "This is an odd number"
        else:
            string += "This is an even number"
        print string

#odd_even()


def multiply(array, b):
    for i in range(len(array)):   
        array[i] = array[i] * b
    
    return array

a = [2, 4, 10, 16]
b = multiply(a, 5)
print b


def layered_multiples(arr):
    
    new_array = []
    for i in range(len(arr)):
        
        temp_array = []
        
        for j in range(0, arr[i]):
            temp_array.append(1)

        
        new_array.append(temp_array)
        

        #while size > 0:   
         #   size = size - 1
          #  print new_array


    print new_array    

        
    



my_list = [2, 4, 5]
multiplier = 3

x = layered_multiples(multiply(my_list, multiplier))
