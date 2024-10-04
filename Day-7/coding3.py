def safe_list_access(my_list,index):
    try:
        return my_list[index]
    except IndexError:

        return "Error:Index out of range"