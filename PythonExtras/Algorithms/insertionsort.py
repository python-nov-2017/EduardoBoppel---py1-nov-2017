
def sort(arr):
    print arr    
    
    for i, value in enumerate(arr):
        for x in range(0, i):
            if arr[i] < arr[x]:
                #USING PYTHON'S BUILT-IN INSERT/POP METHODS
                # arr.insert(x, arr.pop(i))   
                # break        
                
                #USING MANUAL SWAP OF VALUES
                y = i
                while(y>x):
                    arr[y], arr[y-1] = arr[y-1], arr[y]
                    y -= 1
                
    return arr

list = [6,5,3,1,8,7,2,4]
print sort(list)