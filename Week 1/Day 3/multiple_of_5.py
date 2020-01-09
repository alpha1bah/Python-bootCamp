

def multiple(lower, upper):
    mult=[]
    for num in range (lower, upper+1):
        if num % 5==0 :
            mult.append(num)

    return mult

print(multiple(0,100))
