

def find_evens(A,B):
    evens=[]
    for num in range(A, B+1):
        if num % 2 == 0:
            evens.append(num)
    return evens
print("The even list between 2 and 20 are:", find_evens(2,20))


def even_mults(A,B):
    mults=[]
    for nums in range (A,B+1):
        if nums %2 ==0 and nums % 3 == 0 :
            mults.append(nums)
            
    return mults

print("The even and multiple numbers between 2 and 20 are: ",even_mults(2,20))


