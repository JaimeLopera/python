def quicksort(list_to_sort):
    """ The quicksort method 
    lis_to_sort: (list) the provided numbers to sort
    output : (list) the numbers sorted
    """
    length = (len(list_to_sort))//2
    pivot = list_to_sort[length]
    left_list = []
    right_list = []
    middle_list = []
    if length <= 1:
        return list_to_sort
    for i in list_to_sort:
        if i < pivot:
            left_list.append(i)
        elif i > pivot:
            right_list.append(i)
        else:
            middle_list.append(i)
    return quicksort(left_list) + middle_list + quicksort(right_list)

