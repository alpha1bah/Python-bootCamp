# TODO: Write a script to that prints out the multiples of 3 between 0 nad N, where N is a user input

N=int(input("Enter an integer: "))

print("\nUsing the while loop")
counter=0;
while counter <=N:
    if counter % 3 == 0:
        print(counter)
    counter +=1


print("\nUsing foor loop")
for number in range(N+1):
    if number % 3 == 0:
        print(number)