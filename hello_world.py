print('Hello world!')
string1='hello'
int1=5
#string2=str(int11)
#print(string1 + string2)

# Modulo
print(7%6)

number=int(input("Enter a number"))
min_num=3
max_num=15
if number > min_num and number < max_num:
    print('Nice')
elif number > min_num and number < max_num + 2:
    print("Kinda nice")
else:
    print("Not nice")


# While loop 
counter = 0;
while counter <= 0:
    print(counter)
    counter+=1


# for loop
# range (start, stop, increment)
print ('Usinge r')
for number in range (0, 5, 1): # range(0,5)  or range (5)
    print (number)


print ('Usinge r')
for number in range (5): # range(0,5)  or range (5)
    print (number)


# while loop
n=int(input("Enter an upper limit"))
num=0
while num <=n:
    if (num % 2 == 0):
        print(num)
    num+=1