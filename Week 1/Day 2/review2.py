# TODO: Write a script that prints out the commun muktipkes of 3 and 5 between the range 0 and N (Inclusive). Where N is a user input

N=int(input("Enter the upper limit: "))

print("Using while loop")
c=0
while c<= N:
    if c%3==0 and c%5==0:
        print(c)
    c+=1


print("Using for loop")
for num in range (N+1):
    if num %3==0 and num %5==0:
        print(num)