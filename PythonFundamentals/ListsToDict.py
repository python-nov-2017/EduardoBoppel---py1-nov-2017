def make_dict(list1, list2):

    key = []
    value = []

    if len(list1) > len(list2):
        key = list1
        value = list2
    elif len(list1) < len(list2):
        key = list2
        value = list1
    else:
        key = list1
        value = list2

    animal_selections = zip(key, value)
    return animal_selections
    









name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

animal_selections = make_dict(name, favorite_animal)
print animal_selections