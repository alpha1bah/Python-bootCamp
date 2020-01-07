# Function

# define f(x)=x+1

def f(x):
    ans=x+1
    return ans

my_solution=f(1)
print(my_solution)


#Try it for yourself
# define g(x)=x^4+x^2+1

def g(x):
    answer=x**4+x**2+1  # retun (x**4+x**2+1)
    return answer

my_solution2=g(3)
print(my_solution2)
print(g(1),g(2),g(4))



# 3 Return the first two even numbers
# function that has more thatn one return once
def get_first_two_evens():
    return 2, 4

even1, even2 = get_first_two_evens()
print(even1)
print(even2)


#4. Function without return
def print_even(N):
    for num in range (N+1):
        if num % 2 == 0:
            print(num)
print("Even numbers are:")
print_even(10)  # should print 2,4,6,8,10


# TODO: write a function that takes N as an input
def commun_multiple():
    N=int(input("Upper Limit"))
    for n in range (N+1):
        if n%3==0 and n%7==0:
            print(n)


commun_multiple()


# TODO: 
def cmultiple(x,y,N):
    #x=int(input("Enter the first number"))
    #y=int(input("Enter the second number"))
    #N=int(input("Enter the fupper limit"))
    for n in range (N+1):
        if n%x==0 and n%y==0:
            print(n)

cmultiple(3,7,100)


def multiple():
    x=int(input("Enter the first number"))
    y=int(input("Enter the second number"))
    N=int(input("Enter the fupper limit"))
    for n in range (N+1):
        if n%x==0 and n%y==0:
            print(n)

multiple()