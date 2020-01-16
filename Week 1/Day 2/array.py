# Array

my_first_list = [2,4,6,8]
print("The first elemnt is: ",my_first_list[0])
print("The second elemnt is: ",my_first_list[1])
print("The third elemnt is: ",my_first_list[2])
length=len(my_first_list)
print("The lenght of my array is :", length)

for index in range (len(my_first_list)):
    element=my_first_list[index]
    #print(element)

print(my_first_list)

# error
#print(my_first_list[4]) # out of range. The maximum index is 3.     the index are: 0, 1, 2, 3.

my_first_list.append(10)
print("After append:", my_first_list)

# TODO: 
even_list=[]
for num in range (1, 13):
    if num %2==0:
        even_list.append(num)

print("List of even numbers: ", even_list)

#even_list.clear
#print(even_list)
print("Even list before popping up: ", even_list)
for i in range(0, len(even_list)-1):
    if even_list[i]==10:
        index_of_ten=i
        ten=even_list.pop(i)

print("List after popping an element", even_list)
print("The value of the variable ten= ", ten)

even_list.insert(index_of_ten, ten)
print("using insert, to put 10 back: ", even_list)