
def sort(arr):
    print arr    
    for x in range(1, len(arr)-1):
        for i in range(0, len(arr)-1):            
            if arr[i] >= arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    
    return arr

list = [6,5,3,1,8,7,2,4]
print sort(list)