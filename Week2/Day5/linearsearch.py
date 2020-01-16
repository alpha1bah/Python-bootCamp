# This program performs a linear search

def find_element(list, el):
    """
    Implementation of the linear search algorithm.
    \tPARAM: list - list of element to search through
    \tPARAM: el- element to search for
    \RETURN: - index of the e
    """
    #index=None
    for i in range (0, len(list)):
        if list[i] == el :
            return i

  
    return None

    
l=[1,3,2,9,7,13,20]
print(len(l))
print("The list is: ",l)

print(find_element(l,20))