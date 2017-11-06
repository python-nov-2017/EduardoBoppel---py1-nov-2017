
def DictTuple(my_dict):

    new_list = []

    for keys, val in my_dict.items():
        new_list.append((keys, val))

    return new_list




my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

new_list = DictTuple(my_dict)
print new_list