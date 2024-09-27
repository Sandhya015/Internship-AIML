def add_to_list(my_list, item):
    if len(my_list) < 10:
        my_list.append(item)
    else:
        print("The list already has 10 items. Cannot add more.")
    
    return my_list