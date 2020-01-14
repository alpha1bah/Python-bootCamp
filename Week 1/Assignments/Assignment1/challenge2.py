# This function takes an integer n as the input. The output function should be a list of all odd integers between o and n inclusively.
# If n=0, the output list should be empty.

def odd_numbers(number):
    ar=[]
    for i in range(number+1):
        if i % 2 == 1 :
            ar.append(i)
    return ar

# Calling and printing the odd array
print(odd_numbers(20))