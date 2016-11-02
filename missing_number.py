def find_missing(array_1, array_2):
    if len(array_1) == len(array_2):
        return 0
    else:
        longer_list = array_1 
        if len(array_2) > len(longer_list):
            longer_list = array_2
            shorter_list = array_1
        else:
            shorter_list = array_2
        for element in longer_list:
            if element not in shorter_list:
                return element