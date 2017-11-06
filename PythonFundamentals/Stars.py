def draw_stars(my_list):

    print my_list

    for i in my_list:
        if isinstance(i, str):
            print i.lower()[0] * len(i)

        if isinstance(i, (int, long, float)):
            print "*" * i
    


#x = [4, 6, 1, 3, 5, 7, 13]
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(x)