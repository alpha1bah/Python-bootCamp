

import random
winning_number=random.randint(0,10)
print(winning_number)


guesses=[]
guesses_taken=0
#num_guesses=5
user_won=False
total_guesses = 5


#while num_guesses !=0 and user_won == False:
    #user_guess = int(input("Enter your guess: "))
    #dif=user_guess-winning_number


while guesses_taken < total_guesses and user_won !=True:
    user_guess=int(input("Enter your guess: "))
    guesses.append(user_guess)
    guesses_taken +=1
    if user_guess==winning_number:
        user_won=True
        print("Congrats, you won")
    elif user_guess >= winning_number - 5 and user_guess <= winning_number + 5:
        print("Hot")
    elif user_guess >= winning_number - 10 and user_guess <= winning_number +10 :
        print("Warm")
    else:
        print("Cold")


