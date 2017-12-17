
def sort(arr):
    print arr    
    
    for i, value in enumerate(arr):
        min_value = value
        min_index = i

        for x in range(i, len(arr)):
            if arr[x] < min_value:
                min_value = arr[x]
                min_index = x
                            
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
            

    
    return arr

list = [6,5,3,1,8,7,2,4]
print sort(list)