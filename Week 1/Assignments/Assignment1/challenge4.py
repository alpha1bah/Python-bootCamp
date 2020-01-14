# Create a function that compares two lists of integers. The output of the function should be a list containing the difference 
# between the first and second lists. In order wordds, list all the elements that are unique only to ONE of the lists.

# If both lists are empty or the same, the output list should also be empty.

# Fsdinding the differences between 2 lists without the use of sets



def difference(list1, list2):
    list=[]
    for i in range (len(list1)):
        if list1[i] != list2[i]:
            list.append(list1[i])
            list.append(list2[i])

    return list

a=[1,2,3,4,5,6]
b=[1,2,4,4,5,8]
print("The first list is: ", a)
print("The second list is: ",b)


print("The difference between the two lists is: ")
print(difference(a,b))