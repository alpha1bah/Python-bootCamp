# This program is a function that takes a list of integers or floats as the input of the function 
# and the output of the function is the sum of the elements of the list

# Definition of the function
def my_list(list):
	sum=0
	for i in range (len(list)):
		sum+=list[i]

	return sum

# Definition of the list
a=[3,-4,9,8.5,-1]
print("Here is the array: ",a)

# Function call
print("The sum of all the elements of the aray is:" , my_list(a))