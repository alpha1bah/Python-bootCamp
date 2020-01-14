# 

import random

def roll_dice(highest_num):
    """
    rolls a disc using the choice function from the random module
    """

    return random.randint(1, highest_num)


def monte_carlo(N):
    """

    """
    one_counter = 0
    two_counter = 0
    three_counter = 0
    four_counter = 0
    five_counter = 0
    six_counter = 0
    dice_max = 6
    for exp in range (0, n):
        if roll_dice(dice_max) == 1:
            one_counter += 1

        elif roll_dice(dice_max) == 2:
            two_counter += 1

        elif roll_dice(dice_max) == 1:
            three_counter += 1

        elif roll_dice(dice_max) == 1:
            four_counter += 1

        elif roll_dice(dice_max) == 1:
            five_counter += 1

        else:
            six_counter += 1
    


        print(f"Probability of 1 = {(one_counter/N) * 100} %")
        print(f"Probability of 2 = {(two_counter/N) * 100} %")
        print(f"Probability of 3 = {(three_counter/N) * 100} %")
        print(f"Probability of 4 = {(four_counter/N) * 100} %")
        print(f"Probability of 5 = {(five_counter/N) * 100} %")
        print(f"Probability of 6 = {(six_counter/N) * 100} %")





def monte_carlo_with_lists(N, dice_max=6):
    results = []

    for exp in range (0,N):
        results.append(roll_dice(dice_max))

    for outcome in range (1, dice_max+1):
        count = results.count(outcome)
        msg = f"The probability of {outcome} = {(count/N * 100)} %"
        print(msg)


dice_max = 6
print(f"The probability should converge to {1/dice_max *100} %")
monte_carlo_with_lists(10000, dice_max)