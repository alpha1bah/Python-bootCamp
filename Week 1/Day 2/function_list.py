

def find_evens(A,B):
    evens=[]
    for num in range(A, B+1):
        if num % 2 == 0:
            evens.append(num)
    return find_evens
print(find_evens(2,20))


def even_mults(A,B):
    mults=[]
    for nums in range (A,B+1):
        if nums %2 ==0 and nums % 3 == 0 :
            mults.append(nums)
            
    return mults

print(even_mults)

