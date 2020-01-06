# The goal of this program is to print all the numbers between N and M

n=int(input("Enter the lower limit"))
m=int(input("Enter the uper limit"))

print("\nUsing foor loop")
sum=0
for number in range (n,m+1):
    sum+=number
print("The total sum is: ",sum)


print("\nUsing while loop")
sum2=0
counter=n
while counter <= m:
    sum2+=counter
    counter+=1
print("The total sum is: ",sum2)