# 

def find_diffs(a,b):
    differences=[]
    for element in a :
        if element not in b :
            differences.append(element)

    for element in b:
        if element not in a:
            differences.append(element)

    return differences


l1=[1,2,3]
l2=[1,2,3]
print(find_diffs(l1,l2))