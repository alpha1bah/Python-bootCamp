def fmin(list):
    """

    This function returns the maximum element in the list

    \tparam: list- a list of a numerical elements
    \treturns: the maximum value in the list

    """
    min=list[0]
    for index in  range (1,len(list)):
        if list[index]<min:
            min=list[index]
    return min

#help(fmin)

my_list=[10,8,19,42,17,20]
print(fmin(my_list))