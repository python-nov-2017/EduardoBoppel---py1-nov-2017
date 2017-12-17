def insert_val_at(index, my_list, value):
    if index > len(my_list):
        return False

    my_list.insert(index, value)
    return my_list


test_list = [0,1,2,3,4]
result = insert_val_at(5, test_list, 100)
print result
        