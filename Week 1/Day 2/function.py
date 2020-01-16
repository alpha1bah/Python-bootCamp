# Function

# define f(x)=x+1

def f(x):
    ans=x+1
    return ans


#For the function f(x)
# Calling of the function f(x)
my_solution=f(1)
print("f(x)=", my_solution)


#Try it for yourself
# define g(x)=x^4+x^2+1

def g(x):
    answer=x**4+x**2+1  # retun (x**4+x**2+1)
    return answer




# For the function g(x)
# Calling of the function g(x)
my_solution2=g(3)
print("g(3)=",my_solution2)
print("g(1)=", g(1), "g(2)=",g(2), "g(3)=",g(3), "g(4)=", g(4))



# 3-)  Return the first two even numbers
# function that has more thatn one return at a time
def get_first_two_evens():
    return 2, 4

even1, even2 = get_first_two_evens()
print("Even 1 is: ",even1)
print("Even 2 is: ",even2)


#4. Function without return
def print_even(N):
    for num in range (N+1):
        if num % 2 == 0:
            print(num)
print("Even numbers up to 10 are:")
print_even(10)  # should print 2,4,6,8,10


# TODO: write a function that takes N as an input
def commun_multiple_of_3_and_7():
    N=int(input("Upper Limit for the commun multiple of 3 and 7: "))
    for n in range (N+1):
        if n%3==0 and n%7==0:
            print(n)


print("Commun multiple of 3 and 7: ")
commun_multiple_of_3_and_7()


# TODO: 
def cmultiple(x,y,N):
    #x=int(input("Enter the first number"))
    #y=int(input("Enter the second number"))
    #N=int(input("Enter the fupper limit"))
    for n in range (N+1):
        if n%x==0 and n%y==0:
            print(n)

print("Commun multiple of 3 and 7 are: ")
cmultiple(3,7,100)


def multiple():
    x=int(input("Enter the first number"))
    y=int(input("Enter the second number"))
    N=int(input("Enter the fupper limit"))
    for n in range (N+1):
        if n%x==0 and n%y==0:
            print(n)

print("Commun multiple of x and y are: ")
multiple()