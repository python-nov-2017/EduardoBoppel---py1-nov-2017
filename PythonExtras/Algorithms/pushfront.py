def push_front(arr, val):
     #USING BUILD-IN FUNCTIONS
    # arr.insert(0, val) 
    
    #USING MANUAL SWAP
    arr.append(val)
    arr[0], arr[len(arr)-1] =arr[len(arr)-1], arr[0]
    
    return arr



my_list = [5, 104, 7, 34, 245]
val = 3
print (push_front(my_list, val))