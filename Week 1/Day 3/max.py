
def fmax(list):
    """

    This function returns the maximum element in the list

    \tparam: list- a list of a numerical elements
    \treturns: the maximum value in the list

    """
    max=list[0]
    for index in  range (1,len(list)):
        if list[index]>=max:
            max=list[index]
    return max

#help(fmax)

my_list=[10,8,19,42,17,20]
print(fmax(my_list))