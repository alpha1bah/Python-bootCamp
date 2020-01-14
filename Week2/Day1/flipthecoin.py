# import the random module

import random

def flip_coin():
    """
    Return a coin flip - random integer between 0 and 1
    if 1 - the coin lands in heads
    if 0 - the coin lands in tails
    """

    return random.randint(0, 1)


def monte_carlo(n):
    """
    Performs a monte carlos simulation of a coin flip
    [PARAM]\t n (int) - number of samples
    [RETURN]\t NONE - prints out the result of the simulation
    """
    head_count = 0
    tail_count = 0
    exp_count = 0
    while exp_count < n :
        result = flip_coin()

        if result == 1 :
            head_count +=1
        else :
            tail_count +=1

        exp_count +=1

    print(f"There were {n} simulations performed.")
    
    msg = f"There were {(head_count/n)*100} % heads"
    print(msg)
    
    msg = f"There were {(tail_count/n)*100} % tails"
    print(msg)

            
monte_carlo(1000)